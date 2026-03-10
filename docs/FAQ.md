# Frequently Asked Questions

## General Questions

### Which version should I use?
* **HTML GUI**: Simplest option. One file, open in browser. Works everywhere.
* **Desktop GUI**: Standalone app for Windows/Mac. No browser needed.
* **CLI**: For terminal lovers and developers. Works on all OS with Python.

### Are these tools really free?
Yes! All versions are completely free and open source under the MIT license.

### Do you collect any data?
No. **All data stays on your device.** 100% offline. No tracking, no analytics, no cloud.

### Do I need internet to use the tools?
* **HTML GUI**: Internet only needed on first use (to load libraries). After that, works offline.
* **Desktop GUI**: No internet needed at all.
* **CLI**: No internet needed except for initial download of HTML viewer (if missing).

---

## HTML GUI Questions

### Does it work in Firefox/Safari?
Yes! Firefox and Safari are fully supported. However:
* Folder selection is not available (uses ZIP download instead)
* Wake Lock uses audio fallback (still prevents sleep)

### Will my computer sleep during the test?
No. The tool actively prevents sleep:
* **Chrome/Edge**: Uses native Wake Lock API
* **Firefox/Safari**: Uses silent audio loop (works just as well)

### Where are reports saved?
* **Chrome/Edge**: To the folder you select
* **Firefox/Safari**: As ZIP file in Downloads folder

### Why does it stop at 5%?
Deep discharging lithium-ion batteries (below 5%) can permanently damage them. Stopping at 5% is a safety feature.

### Can I close the browser tab during test?
No – the test stops if the tab closes. However, the tool saves progress every minute and will ask to resume when you reopen.

### Why do I see "Using ZIP fallback" in Chrome/Edge?
The folder you previously selected is no longer accessible (deleted, moved, or permissions lost). Click the location bar and pick a new folder.

---

## Desktop GUI Questions

### Do I need to install anything?
No. Just download and run. The app is self-contained.

### Is it safe?
Yes. The app runs entirely on your device. Built from the same open-source code as the HTML version.

### Why does macOS show a security warning?
The app is not signed with an Apple developer certificate. To run:
1. **Right-click** the app
2. Select **"Open"**
3. Click **"Open"** in the dialog

### Can I use it on Linux?
Not yet. The desktop version is currently Windows and macOS only. Linux users can use HTML GUI or CLI.

---

## CLI Questions

### Do I need Python?
Yes. Python 3.6 or higher is required. The installer will check for it.

### What if I don't have Python?
* Install Python from [python.org](https://www.python.org/downloads/)
* Or use the HTML GUI version instead

### How do I install it?
Run the installer for your OS from the `CLI/BIN/` folder:
* **Windows**: Double-click `install-windows.bat`
* **macOS**: `bash install-macos.sh`
* **Linux**: `bash install-linux.sh`

### What commands are available?
```bash
cebt /S     # Start test
cebt /R     # Show results
cebt /C     # Compare tests
cebt /L     # Open last report in browser
cebt /O     # Set output folder
cebt /H     # Show help
```

### Why do I need battery-reporter.html for /L?
The CLI tool uses the HTML file as a viewer to display reports with charts. The first time you run `/L`, you'll be prompted to download it.

### Can I use the CLI offline?
Yes, as long as you have:
* The `cebt` command installed
* `battery-reporter.html` in your current folder
* Existing test reports

---

## Battery Questions

### How accurate is the health estimate?
The health estimate is based on your actual discharge rate during the test. It's more accurate than manufacturer estimates because it measures real-world usage.

### Can I test from any starting percentage?
Yes, but starting at 100% gives the most accurate "full battery life" estimate.

### Can I change the stop percentage?
Currently fixed at 5% for safety. Custom stop percentage is planned for future releases.

### How often should I test my battery?
* Every 3-6 months for normal use
* Before and after major OS updates
* If you notice reduced battery life

### Does this work on multiple batteries?
Currently supports single battery laptops. Multiple battery support is planned.

---

## Technical Questions

### What APIs does the HTML version use?
* Battery API for readings
* Wake Lock API for sleep prevention
* File System Access API for folder selection
* Web Audio API as fallback for Wake Lock
* IndexedDB for storing folder preferences

### What libraries do you use?
* **Chart.js** – for charts
* **JSZip** – for ZIP creation
* **FileSaver.js** – for saving files

All libraries are loaded from CDNs and run locally. No data is sent to these services.

### Is the code open source?
Yes! All code is available on GitHub under the MIT license.

---

## Troubleshooting

### HTML GUI: Battery percentage not showing
Use Chrome, Edge, or Firefox latest version.

### HTML GUI: Wake Lock inactive
* **Chrome/Edge**: Use HTTPS or localhost
* **Firefox**: Audio fallback is working – still prevents sleep

### Desktop GUI: App won't start (Windows)
Download again – file may be corrupted. Allow in antivirus if flagged (false positive).

### Desktop GUI: Can't open on macOS
Right-click and select **"Open"**, or go to **System Settings > Privacy & Security** and click **"Open Anyway"**.

### CLI: "cebt: command not found"
Restart your terminal, or run the installer again.

### CLI: Download fails with SSL error
Use manual download option instead.

---

## Still have questions?
* **GitHub Issues:** [https://github.com/CreatorsEye/battery-reporter/issues](https://github.com/CreatorsEye/battery-reporter/issues)
* **Email:** Creatorseye@gmail.com
