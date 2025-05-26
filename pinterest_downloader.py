import os
import asyncio
import requests
import re
from urllib.parse import urlparse, urljoin
from playwright.async_api import async_playwright
from datetime import datetime
import json

class PinterestDownloader:
    def __init__(self, download_folder=None):
        """Initialize the Pinterest downloader."""
        if download_folder is None:
            # Default to downloads folder in current directory
            self.download_folder = os.path.join(os.getcwd(), "downloads")
        else:
            self.download_folder = download_folder
        
        # Create download folder if it doesn't exist
        os.makedirs(self.download_folder, exist_ok=True)
        
        self.downloaded_images = []
        self.failed_downloads = []
    
    async def extract_images_from_pinterest_url(self, page, url):
        """Extract image URLs from a Pinterest page."""
        print(f"Visiting: {url}")
        
        try:
            await page.goto(url, wait_until="networkidle", timeout=30000)
            await page.wait_for_timeout(3000)  # Wait for images to load
            
            # Scroll down to load more images
            for _ in range(3):
                await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                await page.wait_for_timeout(2000)
            
            # Extract image URLs using multiple selectors
            image_urls = set()
            
            # Method 1: Look for img tags with Pinterest image patterns
            img_elements = await page.query_selector_all('img')
            for img in img_elements:
                src = await img.get_attribute('src')
                if src and self.is_valid_pinterest_image(src):
                    # Get high-resolution version
                    high_res_url = self.get_high_res_url(src)
                    image_urls.add(high_res_url)
            
            # Method 2: Look for data attributes that might contain image URLs
            data_elements = await page.query_selector_all('[data-test-id="pin-closeup-image"]')
            for element in data_elements:
                src = await element.get_attribute('src')
                if src and self.is_valid_pinterest_image(src):
                    high_res_url = self.get_high_res_url(src)
                    image_urls.add(high_res_url)
            
            print(f"Found {len(image_urls)} images on this page")
            return list(image_urls)
            
        except Exception as e:
            print(f"Error extracting images from {url}: {str(e)}")
            return []
    
    def is_valid_pinterest_image(self, url):
        """Check if URL is a valid Pinterest image."""
        if not url:
            return False
        
        # Pinterest image patterns
        pinterest_patterns = [
            'i.pinimg.com',
            'pinterest.com',
            'pinimg.com'
        ]
        
        return any(pattern in url for pattern in pinterest_patterns) and \
               any(ext in url.lower() for ext in ['.jpg', '.jpeg', '.png', '.webp'])
    
    def get_high_res_url(self, url):
        """Convert Pinterest image URL to highest resolution version."""
        # Pinterest URL patterns for high resolution
        # Replace size indicators with largest available
        url = re.sub(r'/\d+x/?', '/originals/', url)
        url = re.sub(r'_\d+\.', '_original.', url)
        
        # Remove size constraints
        if '236x' in url:
            url = url.replace('236x', 'originals')
        if '474x' in url:
            url = url.replace('474x', 'originals')
        if '564x' in url:
            url = url.replace('564x', 'originals')
        
        return url
    
    def download_image(self, url, filename=None):
        """Download an image from URL."""
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.9',
                'Accept-Encoding': 'gzip, deflate, br',
                'DNT': '1',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
                'Referer': 'https://www.pinterest.com/'
            }
            
            response = requests.get(url, headers=headers, stream=True, timeout=30)
            response.raise_for_status()
            
            if filename is None:
                # Generate filename from URL
                parsed_url = urlparse(url)
                filename = os.path.basename(parsed_url.path)
                if not filename or '.' not in filename:
                    filename = f"pinterest_image_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}.jpg"
            
            # Ensure unique filename
            base_name, ext = os.path.splitext(filename)
            counter = 1
            while os.path.exists(os.path.join(self.download_folder, filename)):
                filename = f"{base_name}_{counter}{ext}"
                counter += 1
            
            filepath = os.path.join(self.download_folder, filename)
            
            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            print(f"Downloaded: {filename}")
            self.downloaded_images.append(filepath)
            return filepath
            
        except Exception as e:
            print(f"Failed to download {url}: {str(e)}")
            self.failed_downloads.append(url)
            return None
    
    async def process_pinterest_urls(self, urls):
        """Process multiple Pinterest URLs and download all images."""
        async with async_playwright() as p:
            # Launch browser
            browser = await p.chromium.launch(headless=False)  # Set to True for headless mode
            context = await browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                viewport={"width": 1920, "height": 1080}
            )
            page = await context.new_page()
            
            all_image_urls = []
            
            for url in urls:
                images = await self.extract_images_from_pinterest_url(page, url)
                all_image_urls.extend(images)
            
            await browser.close()
            
            # Remove duplicates
            unique_images = list(set(all_image_urls))
            print(f"\nTotal unique images found: {len(unique_images)}")
            
            # Download all images
            print("Starting downloads...")
            for i, img_url in enumerate(unique_images, 1):
                print(f"Downloading {i}/{len(unique_images)}: {img_url}")
                self.download_image(img_url)
            
            return self.get_summary()
    
    def get_summary(self):
        """Get download summary."""
        return {
            "downloaded_count": len(self.downloaded_images),
            "failed_count": len(self.failed_downloads),
            "downloaded_files": self.downloaded_images,
            "failed_urls": self.failed_downloads,
            "download_folder": self.download_folder
        }

async def main():
    """Main function to run the Pinterest downloader."""
    print("Pinterest Image Downloader")
    print("=" * 50)
    
    # Get Pinterest URLs from user
    print("Enter Pinterest URLs (one per line). Press Enter twice when done:")
    urls = []
    while True:
        url = input().strip()
        if not url:
            break
        if 'pinterest.com' in url:
            urls.append(url)
        else:
            print("Please enter a valid Pinterest URL")
    
    if not urls:
        print("No valid URLs provided!")
        return
    
    # Create downloader instance
    downloader = PinterestDownloader()
    
    print(f"\nProcessing {len(urls)} Pinterest URL(s)...")
    
    # Process URLs and download images
    summary = await downloader.process_pinterest_urls(urls)
    
    # Print summary
    print("\n" + "=" * 50)
    print("DOWNLOAD SUMMARY")
    print("=" * 50)
    print(f"Successfully downloaded: {summary['downloaded_count']} images")
    print(f"Failed downloads: {summary['failed_count']}")
    print(f"Images saved to: {summary['download_folder']}")
    
    if summary['failed_count'] > 0:
        print("\nFailed URLs:")
        for url in summary['failed_urls']:
            print(f"  - {url}")

if __name__ == "__main__":
    asyncio.run(main())
