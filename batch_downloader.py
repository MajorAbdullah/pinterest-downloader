#!/usr/bin/env python3
"""
Pinterest Image Downloader - Batch Mode
This script allows you to provide multiple Pinterest URLs in a file or as command-line arguments.
"""

import asyncio
import sys
import os
from pinterest_downloader import PinterestDownloader

def read_urls_from_file(filepath):
    """Read URLs from a text file."""
    urls = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and 'pinterest.com' in line:
                    urls.append(line)
        return urls
    except Exception as e:
        print(f"Error reading file {filepath}: {e}")
        return []

async def batch_download(urls, output_folder=None):
    """Download images from multiple Pinterest URLs."""
    if not urls:
        print("No valid Pinterest URLs provided!")
        return
    
    print(f"Pinterest Batch Image Downloader")
    print("=" * 50)
    print(f"Processing {len(urls)} URL(s)...")
    
    # Create downloader
    downloader = PinterestDownloader(download_folder=output_folder)
    
    # Process all URLs
    summary = await downloader.process_pinterest_urls(urls)
    
    # Print detailed summary
    print("\n" + "=" * 50)
    print("BATCH DOWNLOAD SUMMARY")
    print("=" * 50)
    print(f"Successfully downloaded: {summary['downloaded_count']} images")
    print(f"Failed downloads: {summary['failed_count']}")
    print(f"Images saved to: {summary['download_folder']}")
    
    if summary['downloaded_files']:
        print(f"\nDownloaded files:")
        for file in summary['downloaded_files'][:10]:  # Show first 10
            print(f"  - {os.path.basename(file)}")
        if len(summary['downloaded_files']) > 10:
            print(f"  ... and {len(summary['downloaded_files']) - 10} more files")
    
    if summary['failed_urls']:
        print(f"\nFailed URLs:")
        for url in summary['failed_urls']:
            print(f"  - {url}")
    
    return summary

def main():
    """Main function for batch processing."""
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python batch_downloader.py <url1> [url2] [url3] ...")
        print("  python batch_downloader.py --file <urls_file.txt>")
        print("  python batch_downloader.py --file <urls_file.txt> --output <output_folder>")
        return
    
    urls = []
    output_folder = None
    
    # Parse command line arguments
    i = 1
    while i < len(sys.argv):
        arg = sys.argv[i]
        
        if arg == '--file':
            if i + 1 < len(sys.argv):
                urls.extend(read_urls_from_file(sys.argv[i + 1]))
                i += 1
            else:
                print("Error: --file requires a filename")
                return
        elif arg == '--output':
            if i + 1 < len(sys.argv):
                output_folder = sys.argv[i + 1]
                i += 1
            else:
                print("Error: --output requires a folder path")
                return
        elif 'pinterest.com' in arg:
            urls.append(arg)
        
        i += 1
    
    if not urls:
        print("No valid Pinterest URLs found!")
        return
    
    # Run the batch download
    asyncio.run(batch_download(urls, output_folder))

if __name__ == "__main__":
    main()
