@echo off
echo Pinterest Image Downloader
echo ========================
echo.
echo Choose an option:
echo 1. Interactive mode (enter URLs manually)
echo 2. Batch mode (provide URLs as arguments)
echo 3. Batch mode from file
echo.
set /p choice="Enter your choice (1-3): "

if "%choice%"=="1" (
    python pinterest_downloader.py
) else if "%choice%"=="2" (
    echo.
    echo Example: python batch_downloader.py "https://pinterest.com/pin/123/" "https://pinterest.com/pin/456/"
    echo.
    set /p urls="Enter Pinterest URLs separated by spaces: "
    python batch_downloader.py %urls%
) else if "%choice%"=="3" (
    echo.
    set /p filename="Enter the filename containing URLs (e.g., urls.txt): "
    python batch_downloader.py --file "%filename%"
) else (
    echo Invalid choice!
)

echo.
pause
