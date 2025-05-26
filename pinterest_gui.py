"""
Pinterest Image Downloader - GUI Version
A simple graphical interface for downloading Pinterest images.
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog, scrolledtext
import asyncio
import threading
from pinterest_downloader import PinterestDownloader
import os

class PinterestDownloaderGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Pinterest Image Downloader")
        self.root.geometry("600x500")
        
        # Variables
        self.download_folder = tk.StringVar(value=os.path.join(os.getcwd(), "downloads"))
        self.urls_text = tk.StringVar()
        self.is_downloading = False
        
        self.setup_ui()
    
    def setup_ui(self):
        """Set up the user interface."""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(2, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="Pinterest Image Downloader", 
                               font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Download folder selection
        folder_frame = ttk.LabelFrame(main_frame, text="Download Folder", padding="5")
        folder_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        folder_frame.columnconfigure(0, weight=1)
        
        folder_entry = ttk.Entry(folder_frame, textvariable=self.download_folder, width=50)
        folder_entry.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=(0, 5))
        
        browse_button = ttk.Button(folder_frame, text="Browse", command=self.browse_folder)
        browse_button.grid(row=0, column=1)
        
        # URL input
        url_frame = ttk.LabelFrame(main_frame, text="Pinterest URLs (one per line)", padding="5")
        url_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        url_frame.columnconfigure(0, weight=1)
        url_frame.rowconfigure(0, weight=1)
        
        self.url_text = scrolledtext.ScrolledText(url_frame, width=60, height=10)
        self.url_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Buttons frame
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=3, column=0, columnspan=2, pady=(0, 10))
        
        self.download_button = ttk.Button(button_frame, text="Download Images", 
                                         command=self.start_download, style="Accent.TButton")
        self.download_button.pack(side=tk.LEFT, padx=(0, 10))
        
        clear_button = ttk.Button(button_frame, text="Clear URLs", command=self.clear_urls)
        clear_button.pack(side=tk.LEFT, padx=(0, 10))
        
        example_button = ttk.Button(button_frame, text="Load Example URLs", 
                                   command=self.load_example_urls)
        example_button.pack(side=tk.LEFT)
        
        # Progress bar
        self.progress = ttk.Progressbar(main_frame, mode='indeterminate')
        self.progress.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Status label
        self.status_label = ttk.Label(main_frame, text="Ready to download", foreground="green")
        self.status_label.grid(row=5, column=0, columnspan=2)
    
    def browse_folder(self):
        """Browse for download folder."""
        folder = filedialog.askdirectory(initialdir=self.download_folder.get())
        if folder:
            self.download_folder.set(folder)
    
    def clear_urls(self):
        """Clear the URL text area."""
        self.url_text.delete(1.0, tk.END)
    
    def load_example_urls(self):
        """Load example Pinterest URLs."""
        example_urls = [
            "https://www.pinterest.com/search/pins/?q=modern%20architecture",
            "https://www.pinterest.com/search/pins/?q=interior%20design",
            "https://www.pinterest.com/search/pins/?q=web%20design%20inspiration"
        ]
        self.url_text.delete(1.0, tk.END)
        self.url_text.insert(1.0, "\\n".join(example_urls))
    
    def get_urls_from_text(self):
        """Extract URLs from the text area."""
        text = self.url_text.get(1.0, tk.END).strip()
        urls = []
        for line in text.split('\\n'):
            line = line.strip()
            if line and 'pinterest.com' in line:
                urls.append(line)
        return urls
    
    def start_download(self):
        """Start the download process in a separate thread."""
        if self.is_downloading:
            return
        
        urls = self.get_urls_from_text()
        if not urls:
            messagebox.showwarning("No URLs", "Please enter at least one Pinterest URL.")
            return
        
        if not os.path.exists(self.download_folder.get()):
            try:
                os.makedirs(self.download_folder.get(), exist_ok=True)
            except Exception as e:
                messagebox.showerror("Folder Error", f"Cannot create download folder: {e}")
                return
        
        # Start download in separate thread
        self.is_downloading = True
        self.download_button.config(state='disabled', text='Downloading...')
        self.progress.start()
        self.status_label.config(text=f"Starting download of {len(urls)} URL(s)...", foreground="blue")
        
        # Run download in thread
        thread = threading.Thread(target=self.run_download, args=(urls,))
        thread.daemon = True
        thread.start()
    
    def run_download(self, urls):
        """Run the download process."""
        try:
            # Create new event loop for this thread
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            
            # Create downloader and start download
            downloader = PinterestDownloader(download_folder=self.download_folder.get())
            summary = loop.run_until_complete(downloader.process_pinterest_urls(urls))
            
            # Update UI on main thread
            self.root.after(0, self.download_completed, summary)
            
        except Exception as e:
            self.root.after(0, self.download_error, str(e))
        finally:
            loop.close()
    
    def download_completed(self, summary):
        """Handle download completion."""
        self.is_downloading = False
        self.download_button.config(state='normal', text='Download Images')
        self.progress.stop()
        
        message = (f"Download completed!\\n\\n"
                  f"Successfully downloaded: {summary['downloaded_count']} images\\n"
                  f"Failed downloads: {summary['failed_count']}\\n"
                  f"Images saved to: {summary['download_folder']}")
        
        self.status_label.config(text=f"Downloaded {summary['downloaded_count']} images", 
                                foreground="green")
        
        messagebox.showinfo("Download Complete", message)
        
        # Ask if user wants to open the download folder
        if summary['downloaded_count'] > 0:
            if messagebox.askyesno("Open Folder", "Would you like to open the download folder?"):
                try:
                    os.startfile(summary['download_folder'])
                except:
                    # Fallback for other operating systems
                    import subprocess
                    subprocess.run(['explorer', summary['download_folder']], check=False)
    
    def download_error(self, error_message):
        """Handle download error."""
        self.is_downloading = False
        self.download_button.config(state='normal', text='Download Images')
        self.progress.stop()
        self.status_label.config(text="Download failed", foreground="red")
        
        messagebox.showerror("Download Error", f"An error occurred during download:\\n\\n{error_message}")

def main():
    """Main function to run the GUI."""
    root = tk.Tk()
    
    # Set up modern theme
    style = ttk.Style()
    style.theme_use('winnative')  # Use native Windows theme
    
    app = PinterestDownloaderGUI(root)
    
    try:
        root.mainloop()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
