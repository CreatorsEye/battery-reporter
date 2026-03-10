#!/usr/bin/env python3
"""
CEBT - Creators Eye Battery Tester
Command line tool for battery testing
"""

import sys
import os
import time
import webbrowser
import urllib.request
import glob
from datetime import datetime
import platform
import json
from pathlib import Path

HTML_FILENAME = "battery-reporter.html"
GITHUB_HTML_URL = "https://raw.githubusercontent.com/CreatorsEye/battery-reporter/main/GUI/HTML/battery-reporter.html"
GITHUB_PAGE_URL = "https://github.com/CreatorsEye/battery-reporter/blob/main/GUI/HTML/battery-reporter.html"

def check_html_file():
    """Check if HTML file exists in current directory"""
    return os.path.exists(HTML_FILENAME)

def handle_missing_html():
    """Offer options when HTML file is missing"""
    print("\n" + "="*60)
    print("❌ battery-reporter.html not found!")
    print("="*60)
    print("\nThis file is needed to display battery reports.")
    print(f"\nCurrent folder: {os.getcwd()}")
    print("\nOptions:")
    print("  [1] Manual download - Open GitHub page + instructions")
    print("  [2] Auto-download - Save directly to this folder")
    print("  [3] Cancel - Exit")
    print("\n" + "="*60)
    
    while True:
        choice = input("\nEnter choice (1/2/3): ").strip()
        
        if choice == "1":
            return manual_download()
        elif choice == "2":
            return auto_download()
        elif choice == "3":
            print("\n❌ Cancelled.")
            return False
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")

def manual_download():
    """Open browser with instructions for manual download"""
    webbrowser.open(GITHUB_PAGE_URL)
    
    target_folder = os.getcwd()
    target_path = os.path.join(target_folder, HTML_FILENAME)
    
    print("\n" + "="*60)
    print("📋 MANUAL DOWNLOAD INSTRUCTIONS")
    print("="*60)
    print(f"\n1. Browser opened to GitHub page")
    print(f"2. Click the 'Raw' button or download icon")
    print(f"3. Save the file to this exact folder:")
    print(f"   {target_folder}")
    print(f"4. Make sure the file is named: {HTML_FILENAME}")
    print(f"5. Then press Enter to continue")
    print("\n" + "="*60)
    
    input("\nPress Enter after you've placed the file...")
    
    if os.path.exists(target_path):
        print(f"\n✅ File found! Continuing...")
        return True
    else:
        print(f"\n❌ File still not found at: {target_path}")
        retry = input("Try again? (y/n): ").lower()
        if retry == 'y':
            return manual_download()
        else:
            return False

def auto_download():
    """Auto-download HTML file from GitHub"""
    try:
        print("\n📥 Downloading battery-reporter.html...")
        urllib.request.urlretrieve(GITHUB_HTML_URL, HTML_FILENAME)
        print("✅ Download complete!")
        return True
    except Exception as e:
        print(f"\n❌ Download failed: {e}")
        print("Please try manual download instead.")
        return False

def open_last_report():
    """Open the most recent HTML report"""
    print("\n📂 Opening last battery report...")
    
    # Check for HTML file first
    if not check_html_file():
        if not handle_missing_html():
            return
    
    # Find reports folder
    home = str(Path.home())
    if platform.system() == "Windows":
        reports_folder = os.path.join(home, "Documents", "CEBT-Reports")
    elif platform.system() == "Darwin":  # macOS
        reports_folder = os.path.join(home, "Documents", "CEBT-Reports")
    else:  # Linux
        reports_folder = os.path.join(home, "CEBT-Reports")
    
    if not os.path.exists(reports_folder):
        print(f"\n❌ No reports folder found at: {reports_folder}")
        print("Run a test first with: cebt /S")
        return
    
    report_files = list(Path(reports_folder).glob("*_report.html"))
    if not report_files:
        print("\n❌ No report files found.")
        print("Run a test first with: cebt /S")
        return
    
    # Get most recent
    latest_report = max(report_files, key=lambda p: p.stat().st_mtime)
    
    # Open in browser using the HTML file
    html_path = os.path.abspath(HTML_FILENAME)
    print(f"\n📄 Using viewer: {html_path}")
    print(f"📄 Opening report: {latest_report.name}")
    
    # Open the HTML file with the report as parameter (optional)
    webbrowser.open(f"file://{html_path}")
    print("✅ Report opened in your browser")

def main():
    if len(sys.argv) < 2:
        print("cebt /H for help")
        return
    
    cmd = sys.argv[1].upper()
    
    if cmd == "/S":
        print("🔋 Starting test... (coming soon)")
    elif cmd == "/R":
        print("📊 Showing results... (coming soon)")
    elif cmd == "/C":
        print("📊 Comparing tests... (coming soon)")
    elif cmd == "/L":
        open_last_report()
    elif cmd == "/O":
        if len(sys.argv) < 3:
            print(f"📁 Current output folder: {os.path.join(str(Path.home()), 'Documents', 'CEBT-Reports')}")
            print("To change: cebt /O \"C:\\your\\folder\"")
        else:
            print(f"📁 Output folder set to: {sys.argv[2]}")
    elif cmd == "/H":
        show_help()
    else:
        print(f"Unknown command: {cmd}")
        print("Use: cebt /H for help")

def show_help():
    print("""
╔════════════════════════════════════╗
║   CEBT - Creators Eye Battery Tester   ║
╚════════════════════════════════════╝

COMMANDS:
  cebt /S              Start a new battery test
  cebt /R              Show last test results
  cebt /C              Compare all tests
  cebt /L              Open last report in browser
  cebt /O "folder"     Set output folder
  cebt /H              Show this help

EXAMPLES:
  cebt /S
  cebt /O "C:\\my-tests"
  cebt /L

NOTES:
  - First time using /L? The tool will help you get battery-reporter.html
  - Reports are saved to: Documents/CEBT-Reports/

For more information, visit:
https://github.com/CreatorsEye/battery-reporter
""")

if __name__ == "__main__":
    main()
