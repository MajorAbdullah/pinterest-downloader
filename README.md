# Pinterest Image Downloader

**Automated high-resolution image downloading from Pinterest with CLI, batch, and GUI interfaces**

Pinterest Image Downloader is a Python tool that uses Playwright and Chromium to scrape and download images from Pinterest pins, boards, and search results. It automatically detects image URLs, converts them to the highest available resolution, and saves them to a local folder. Three interfaces are included: an interactive command line, a batch processor for multiple URLs, and a graphical user interface built with Tkinter.

---

## Features

- **Automatic Image Extraction** -- scrapes image URLs from Pinterest pages using multiple CSS selector strategies
- **High-Resolution Downloads** -- rewrites Pinterest CDN URLs to request original-quality images instead of thumbnails
- **Batch Processing** -- process multiple Pinterest URLs from command-line arguments or a text file
- **Graphical User Interface** -- Tkinter-based GUI with folder selection, progress bar, and download summaries
- **Smart Filtering** -- validates Pinterest image URLs and skips non-image assets automatically
- **Duplicate Prevention** -- deduplicates image URLs across multiple pages before downloading
- **Unique Filenames** -- generates conflict-free filenames with automatic counter suffixes
- **Error Handling** -- robust retry logic with detailed download summaries showing successes and failures
- **Headless or Visible Browser** -- run Chromium in headless mode for automation or visible mode for debugging
- **Cross-Platform** -- works on Windows, macOS, and Linux

---

## Tech Stack

![Python](https://img.shields.io/badge/Python-3.7+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-1.40-2EAD33?style=for-the-badge&logo=playwright&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-3776AB?style=for-the-badge&logo=python&logoColor=white)

| Component | Technology |
|-----------|-----------|
| Browser Automation | Playwright (Chromium) |
| HTTP Downloads | Requests 2.31 |
| Image Processing | Pillow 10.1 |
| HTML Parsing | BeautifulSoup4 4.12 |
| GUI | Tkinter (standard library) |
| Async Runtime | asyncio |

---

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Stable internet connection
- 1 GB free disk space (for Chromium browser and downloaded images)

### Installation

```bash
# Clone the repository
git clone https://github.com/MajorAbdullah/pinterest-downloader.git
cd pinterest-downloader

# Install Python dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install chromium
```

### Windows Quick Setup

1. Double-click `install.bat` to install all dependencies
2. Double-click `run.bat` to launch the program

---

## Usage

### 1. Graphical Interface (Recommended for most users)

```bash
python pinterest_gui.py
```

- Paste Pinterest URLs into the text area (one per line)
- Choose a download folder using the Browse button
- Click **Download Images** and monitor the progress bar
- A summary dialog appears when downloading is complete

### 2. Interactive Command Line

```bash
python pinterest_downloader.py
```

Enter Pinterest URLs one per line when prompted. Press Enter on an empty line to begin downloading.

### 3. Batch Processing

```bash
# Direct URLs as arguments
python batch_downloader.py "https://pinterest.com/pin/123/" "https://pinterest.com/pin/456/"

# URLs from a text file
python batch_downloader.py --file urls.txt

# Custom output folder
python batch_downloader.py --file urls.txt --output "/path/to/download/folder"
```

---

## Supported Pinterest URL Formats

| Type | Example |
|------|---------|
| Individual Pin | `https://www.pinterest.com/pin/123456789/` |
| User Board | `https://www.pinterest.com/username/board-name/` |
| Search Results | `https://www.pinterest.com/search/pins/?q=search-term` |
| Category Page | `https://www.pinterest.com/category/` |

### URL File Format

Create a plain text file with one URL per line:

```
https://www.pinterest.com/username/board-name/
https://www.pinterest.com/pin/123456789/
https://www.pinterest.com/search/pins/?q=architecture
https://www.pinterest.com/search/pins/?q=interior%20design
```

---

## Output

- Images are saved to the `downloads/` folder by default (customizable via CLI flag or GUI)
- Each image receives a unique filename to prevent overwrites
- Original file extensions and quality are maintained
- A detailed summary is printed on completion:

```
==================================================
DOWNLOAD SUMMARY
==================================================
Successfully downloaded: 87 images
Failed downloads: 18
Images saved to: /path/to/downloads
```

---

## Project Structure

```
pinterest-downloader/
├── pinterest_downloader.py   # Core downloader class (extraction, resolution upgrade, download)
├── pinterest_gui.py          # Tkinter GUI application
├── batch_downloader.py       # Batch processing CLI with --file and --output flags
├── requirements.txt          # Python dependencies
├── install.bat               # Windows one-click dependency installer
├── run.bat                   # Windows one-click launcher
└── README.md
```

---

## How It Works

1. **Page Loading** -- Playwright launches Chromium and navigates to the Pinterest URL, waiting for network idle
2. **Scrolling** -- the page is scrolled multiple times to trigger lazy-loaded image rendering
3. **Extraction** -- all `<img>` elements and Pinterest-specific data attributes are queried for image source URLs
4. **Resolution Upgrade** -- thumbnail URLs (236x, 474x, 564x) are rewritten to request `/originals/` resolution
5. **Deduplication** -- image URLs are collected into a set to eliminate duplicates across pages
6. **Download** -- each image is fetched with browser-like headers and saved with a unique filename

---

## Troubleshooting

### No images downloaded
- Verify the Pinterest URLs are accessible and point to public content
- Check your internet connection
- Some Pinterest content may be region-restricted

### 403 Forbidden errors
- Normal for copyright-protected Pinterest images -- the program skips these and continues
- Try different search terms or board URLs

### Browser installation issues
- Run `playwright install chromium --force` to reinstall
- Ensure sufficient disk space is available
- On Windows, try running as administrator

### Slow downloads
- Pinterest may throttle requests during peak hours
- Process URLs in smaller batches (10-20 at a time)
- Use specific board URLs for better success rates

---

## System Requirements

| Requirement | Minimum | Recommended |
|------------|---------|-------------|
| Python | 3.7+ | 3.10+ |
| RAM | 2 GB | 4 GB |
| Storage | 1 GB free | Depends on download volume |
| OS | Windows 10+, macOS 10.14+, Linux | Any modern OS |
| Network | Stable connection | Broadband |

---

## Legal Notice

This tool is intended for educational and personal use only. Users are responsible for complying with Pinterest's Terms of Service, applicable copyright laws, and local regulations regarding web scraping. Always obtain proper permissions before using downloaded images commercially.

---

## Changelog

| Version | Changes |
|---------|---------|
| 1.0 | Initial release with core downloading functionality |
| 1.1 | Added GUI interface and batch processing |
| 1.2 | Improved error handling and progress tracking |
| 1.3 | Enhanced image quality detection and download speeds |

---

## License

MIT License

## Author

**Syed Abdullah Shah** -- [@MajorAbdullah](https://github.com/MajorAbdullah)
