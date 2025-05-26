@echo off
echo Installing Pinterest Downloader dependencies...
echo.

echo Installing Python packages...
pip install -r requirements.txt

echo.
echo Installing Playwright browsers...
playwright install chromium

echo.
echo Installation complete!
echo.
echo Usage:
echo   Interactive mode: python pinterest_downloader.py
echo   Batch mode: python batch_downloader.py --file urls.txt
echo.
pause
