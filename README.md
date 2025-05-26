# Pinterest Image Downloader

A comprehensive Python program that uses Playwright to automatically download images from Pinterest posts, boards, and search results. Features both command-line and graphical user interfaces.

## ✨ Features

- **🎯 Automatic Image Extraction**: Scrapes images from Pinterest URLs with smart detection
- **📸 High Resolution Downloads**: Automatically finds and downloads the highest resolution versions
- **⚡ Batch Processing**: Process multiple Pinterest URLs simultaneously
- **🔍 Smart Filtering**: Only downloads valid Pinterest images, skips duplicates
- **🖥️ Multiple Interfaces**: Command-line, batch processing, and GUI options
- **📊 Progress Tracking**: Real-time download progress and detailed summaries
- **🛡️ Error Handling**: Robust error handling with retry mechanisms
- **🎨 User-Friendly**: Easy-to-use graphical interface included

## 🚀 Quick Start

### Windows Users (Easy Setup)
1. Double-click `install.bat` to install all dependencies
2. Double-click `run.bat` to start the program

### Manual Installation
1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Install Playwright browsers:
```bash
playwright install chromium
```

## 📖 Usage Options

### 1. Graphical Interface (Recommended)
Launch the user-friendly GUI:
```bash
python pinterest_gui.py
```
- Paste Pinterest URLs in the text area
- Choose download folder
- Click "Download Images"
- View progress and results

### 2. Interactive Command Line
Run the main script for guided experience:
```bash
python pinterest_downloader.py
```
Enter Pinterest URLs one by one when prompted.

### 3. Batch Processing
Process multiple URLs from command line:
```bash
# Direct URLs
python batch_downloader.py "https://pinterest.com/pin/123/" "https://pinterest.com/pin/456/"

# From file
python batch_downloader.py --file urls.txt

# Custom output folder
python batch_downloader.py --file urls.txt --output "C:\Users\YourName\Desktop\Pinterest Images"
```

## 📝 Supported Pinterest URLs

- **Individual Pins**: `https://www.pinterest.com/pin/[pin-id]/`
- **User Boards**: `https://www.pinterest.com/[username]/[board-name]/`
- **Search Results**: `https://www.pinterest.com/search/pins/?q=[search-term]`
- **Category Pages**: `https://www.pinterest.com/[category]/`

### URL File Format
Create a text file with one Pinterest URL per line:
```
https://www.pinterest.com/username/board-name/
https://www.pinterest.com/pin/123456789/
https://www.pinterest.com/search/pins/?q=architecture
https://www.pinterest.com/search/pins/?q=interior%20design
```

## 📂 Output

- Images are downloaded to the `downloads` folder by default (customizable)
- Each image gets a unique filename to prevent conflicts
- Maintains original file extensions and quality
- Detailed summary reports on completion

## 🛠️ Technical Details

- **Browser Engine**: Chromium via Playwright for reliable scraping
- **Image Processing**: Automatic high-resolution URL conversion
- **Async Operations**: Concurrent downloads for maximum efficiency
- **Smart Retry**: Handles network issues and rate limiting
- **Cross-Platform**: Works on Windows, macOS, and Linux

## 📊 Example Results

```
Pinterest Batch Image Downloader
==================================================
Processing 3 URL(s)...
Visiting: https://www.pinterest.com/search/pins/?q=modern%20architecture
Found 61 images on this page
Visiting: https://www.pinterest.com/search/pins/?q=interior%20design  
Found 44 images on this page
Total unique images found: 105
Starting downloads...
Downloaded: modern_house_01.jpg
Downloaded: interior_design_02.jpg
...
==================================================
DOWNLOAD SUMMARY
==================================================
Successfully downloaded: 87 images
Failed downloads: 18
Images saved to: C:\Users\YourName\Desktop\Pinterest Images
```

## 🔧 Troubleshooting

### Common Issues

1. **No images downloaded**
   - Verify Pinterest URLs are accessible and public
   - Check internet connection
   - Some Pinterest content may be region-restricted

2. **403 Forbidden errors**
   - Normal for some Pinterest images (copyright protection)
   - Try different search terms or URLs
   - The program will skip these and continue with others

3. **Browser/Installation issues**
   - Run: `playwright install chromium --force`
   - Ensure you have sufficient disk space
   - Try running as administrator on Windows

4. **Slow downloads**
   - Pinterest may throttle requests during peak hours
   - Try downloading smaller batches
   - Check your internet connection speed

### Performance Tips

- Use specific Pinterest board URLs for better success rates
- Download during off-peak hours for faster speeds
- Process URLs in smaller batches (10-20 at a time)
- Use SSD storage for faster file operations

## 📋 Requirements

- **Python**: 3.7 or higher
- **OS**: Windows 10+, macOS 10.14+, or Linux
- **Memory**: 2GB RAM minimum, 4GB recommended
- **Storage**: 1GB free space for browser and images
- **Network**: Stable internet connection

## ⚖️ Legal Notice

This tool is for educational and personal use only. Please ensure you comply with:
- Pinterest's Terms of Service
- Copyright laws and image usage rights
- Respect for content creators' intellectual property
- Local laws regarding web scraping

Always obtain proper permissions before using downloaded images commercially.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📧 Support

If you encounter any issues or have questions:
1. Check the troubleshooting section above
2. Search existing issues on GitHub
3. Create a new issue with detailed information

## 🔄 Updates

- **v1.0**: Initial release with basic functionality
- **v1.1**: Added GUI interface and batch processing
- **v1.2**: Improved error handling and progress tracking
- **v1.3**: Enhanced image quality detection and download speeds
