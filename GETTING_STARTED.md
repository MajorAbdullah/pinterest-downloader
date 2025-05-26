# 🚀 Getting Started with Pinterest Image Downloader

Welcome! This guide will help you get up and running with the Pinterest Image Downloader in just a few minutes.

## 📋 What You Need

- Windows 10 or later
- Internet connection
- About 10-15 minutes for setup

## 🔧 Quick Setup (Recommended)

### Option 1: Automatic Setup (Easiest)
1. **Download** all files to your computer
2. **Double-click** `install.bat` and wait for it to finish
3. **Double-click** `run.bat` to start using the program
4. That's it! 🎉

### Option 2: Manual Setup
If the automatic setup doesn't work:

1. **Install Python** (if not already installed):
   - Go to https://python.org/downloads
   - Download Python 3.7 or later
   - During installation, check "Add Python to PATH"

2. **Open Command Prompt**:
   - Press `Windows + R`
   - Type `cmd` and press Enter

3. **Navigate to the program folder**:
   ```
   cd "C:\path\to\pinterest-downloader"
   ```

4. **Install dependencies**:
   ```
   pip install playwright requests pillow beautifulsoup4
   playwright install chromium
   ```

## 🎯 How to Use

### Method 1: Graphical Interface (Easiest)
1. Run `python pinterest_gui.py` or use `run.bat`
2. A window will open with a user-friendly interface
3. Paste Pinterest URLs in the text box (one per line)
4. Choose where to save images
5. Click "Download Images"
6. Wait for completion and enjoy your downloaded images!

### Method 2: Command Line
1. Run `python pinterest_downloader.py`
2. Type or paste Pinterest URLs when prompted
3. Press Enter twice when done
4. Wait for the download to complete

## 📝 What URLs Work?

You can download from these Pinterest URL types:

✅ **Individual Pins**
```
https://www.pinterest.com/pin/123456789/
```

✅ **User Boards**
```
https://www.pinterest.com/username/board-name/
```

✅ **Search Results**
```
https://www.pinterest.com/search/pins/?q=modern+architecture
https://www.pinterest.com/search/pins/?q=interior+design
```

## 💡 Tips for Best Results

### 🎯 Getting Good URLs
1. **Go to Pinterest** in your web browser
2. **Search** for what you want (e.g., "modern houses")
3. **Copy the URL** from your browser's address bar
4. **Paste it** into the downloader

### 📁 Organizing Downloads
- Create different folders for different topics
- Use descriptive search terms
- Download smaller batches for better organization

### ⚡ Performance Tips
- **Start small**: Try 1-2 URLs first to test
- **Use specific searches**: "modern kitchen design" vs just "kitchen"
- **Be patient**: Large boards may take several minutes
- **Check your internet**: Faster connection = faster downloads

## 🔍 Example Walkthrough

Let's download some modern architecture images:

1. **Start the program**: Double-click `run.bat`
2. **Choose option 1** (Interactive mode)
3. **Go to Pinterest** and search for "modern architecture"
4. **Copy the URL**: Should look like `https://www.pinterest.com/search/pins/?q=modern%20architecture`
5. **Paste it** into the program and press Enter
6. **Press Enter twice** to start downloading
7. **Wait** for completion
8. **Check** the `downloads` folder for your images!

## 📊 Understanding Results

When downloading finishes, you'll see:
```
==================================================
DOWNLOAD SUMMARY
==================================================
Successfully downloaded: 45 images
Failed downloads: 8
Images saved to: C:\Users\YourName\Desktop\pinterest-downloader\downloads
```

- **Successfully downloaded**: Number of images saved to your computer
- **Failed downloads**: Some images may be protected or unavailable (normal)
- **Images saved to**: Where your images are located

## ❗ Common Issues & Solutions

### "No images downloaded"
- **Check URL**: Make sure it's a valid Pinterest URL
- **Try different URL**: Some boards may be private
- **Check internet**: Ensure you're connected

### "Browser errors"
- **Restart program**: Close and reopen
- **Reinstall browser**: Run `playwright install chromium`
- **Check antivirus**: Some antivirus software blocks automated browsers

### "Permission errors"
- **Run as administrator**: Right-click program and "Run as administrator"
- **Check folder permissions**: Make sure you can write to the download folder
- **Choose different folder**: Try downloading to Desktop or Documents

### "Slow downloads"
- **Normal behavior**: Pinterest may limit download speed
- **Try smaller batches**: Download 10-20 URLs at a time
- **Check during off-peak hours**: Downloads may be faster at different times

## 🎉 You're Ready!

That's it! You now have a powerful Pinterest image downloader. Here are some ideas for what to download:

- 🏠 **Home Design Inspiration**: Interior design, architecture, gardens
- 🎨 **Art & Design**: Digital art, logos, color palettes
- 🍳 **Recipes**: Food photography, recipe collections
- 👗 **Fashion**: Outfit ideas, style inspiration
- 📱 **UI/UX Design**: App interfaces, web design examples

## 📞 Need Help?

If you run into issues:
1. **Read this guide again** - Most issues are covered here
2. **Check the README.md** - Contains detailed technical information
3. **Try the troubleshooting section** - Common problems and solutions
4. **Start with small tests** - Try downloading just 1-2 URLs first

Happy downloading! 🎉📸
