# CEBT – CLI for End Users

## 📥 Installers

| OS | File | What to Do |
|----|------|------------|
| Windows | `install-windows.bat` | Double-click to install |
| macOS | `install-macos.sh` | Run: `bash install-macos.sh` |
| Linux | `install-linux.sh` | Run: `bash install-linux.sh` |

---

## 🚀 After Installation

Open any terminal and type:

```bash
cebt /S     # Start test
cebt /R     # Show results
cebt /C     # Compare tests
cebt /L     # Open last report in browser
cebt /O     # Set output folder
cebt /H     # Show help
```

📄 HTML File for Reports
The first time you run cebt /L, you'll be prompted to get the required HTML file:



❌ battery-reporter.html not found!

Options:
[1] Manual download - Open GitHub page + instructions
[2] Auto-download - Save directly to this folder
[3] Cancel - Exit
Choose:

Option 1: Browser opens to GitHub – you download and place the file manually

Option 2: Automatic download – saves directly to current folder

Option 3: Exit without doing anything

After the HTML file is in place, cebt /L will open your reports in the browser.

📂 Default Output Folder
Reports are saved to: Documents/CEBT-Reports/

You can change this with: cebt /O "C:\your-folder"

text

---

## ✅ **Everything is ready for GitHub!**

All files are:
- Clean and professional
- No ASCII errors
- HTML handling logic included
- Ready to upload
