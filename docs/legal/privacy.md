# Privacy Policy

**Last updated: March 2026**

---

## Our Commitment

At Creators Eye, we believe privacy is a fundamental right.  
**All CEBT tools collect NO data. Nothing leaves your device.**

We don't have servers. We don't have databases. We don't even have a way to receive your data even if we wanted to.

---

## Quick Summary

| Question | Answer |
|----------|--------|
| Do you collect my battery data? | ❌ No |
| Do you store my personal information? | ❌ No |
| Do you use tracking cookies? | ❌ No |
| Do you send data to the cloud? | ❌ No |
| Does the tool work offline? | ✅ Yes |
| Is my data saved on my computer? | ✅ Yes (with your permission) |

---

## Data Storage (All Versions)

### What data is stored locally?

| Data | Where It Goes | Why |
|------|---------------|-----|
| Battery percentage | In memory during test | To track discharge |
| Test logs (timestamps, percentages) | Your chosen folder as `.txt` file | So you have a record |
| Reports with charts | Your chosen folder as `.html` file | For easy viewing |
| Folder preference | Your browser (IndexedDB) or config file | So you don't pick every time |
| Terms acceptance | Your browser (localStorage) or config file | So you only agree once |
| Test history | Your browser (localStorage) or config file | For comparison charts |

**All stored data is local to your device. We never have access to it.**

---

### What data is NOT collected

- ❌ No personal information (name, email, address, phone)
- ❌ No IP addresses
- ❌ No location data
- ❌ No browsing history
- ❌ No tracking cookies
- ❌ No analytics scripts
- ❌ No cloud uploads
- ❌ Nothing sent to Creators Eye servers
- ❌ Nothing sent to any third-party servers

---

## HTML GUI Version

### Third-Party Libraries

The HTML version loads these libraries from public CDNs:

| Library | Purpose | Data Sent |
|---------|---------|-----------|
| [Chart.js](https://www.chartjs.org/) | Drawing charts | None – runs locally |
| [JSZip](https://stuk.github.io/jszip/) | Creating ZIP files | None – runs locally |
| [FileSaver.js](https://github.com/eligrey/FileSaver.js/) | Saving files | None – runs locally |

These libraries are fetched once and then run entirely in your browser. **No data is transmitted to their servers** after the initial download.

If you want 100% offline, use the offline version or download the libraries manually.

### Browser APIs Used

| API | Purpose | Permission Needed |
|-----|---------|-------------------|
| Battery API | Read battery level | None – automatic |
| Wake Lock API | Prevent sleep | None – automatic |
| File System Access API | Choose save folder | User clicks "Allow" |
| IndexedDB | Store preferences | None – automatic |
| Web Audio API | Wake Lock fallback | User clicks START |

### Folder Permissions

When you choose a save folder:
- The browser asks for permission
- Permission is stored locally
- You can revoke it anytime in browser settings
- If permission is lost, tool falls back to ZIP

---

## Desktop GUI Version

The desktop apps are built from the same code as the HTML version, wrapped in a native window.

**No additional data collection.**

- No analytics
- No crash reports
- No usage tracking
- No internet connection required

---

## CLI Version

The CLI tool is a Python script that runs entirely on your computer.

**No additional data collection.**

- No telemetry
- No usage tracking
- No internet connection required (except for initial download of HTML viewer)

### Configuration File

The CLI stores settings in:
- Windows: `%USERPROFILE%\.cebt\config.json`
- macOS/Linux: `~/.cebt/config.json`

This file contains only:
- Your preferred output folder
- Your preferred stop percentage
- Theme preference (future)

**No personal data is ever stored.**

---

## Your Control

### You can:
- ✅ Choose where reports are saved
- ✅ Delete any saved reports anytime
- ✅ Clear browser data to remove preferences
- ✅ Uninstall the CLI tool completely
- ✅ Use the tool offline
- ✅ Inspect the code (it's open source)

### To clear stored data:

**HTML GUI:**
- Clear browser history/cache
- Or use private/incognito mode

**Desktop GUI:**
- Delete the app (no data is stored outside your chosen folder)

**CLI:**
- Delete the `~/.cebt` folder
- Uninstall with your OS package manager

---

## Third-Party Services

**None.** The tools do not use any third-party services, APIs, or servers.

The only exception is the CDN-hosted libraries in the HTML version, which are:
- Optional (offline version available)
- Loaded once and cached
- Send no data

---

## Children's Privacy

Our tools are safe for all ages. We do not collect any personal information from anyone, including children under 13.

---

## Changes to This Policy

If we ever update this privacy policy (which is unlikely), we'll:
1. Update the "Last updated" date
2. Post a notice in the repository
3. Never change our core commitment: **your data stays yours**

Any changes will be minor and will not affect the offline, private nature of the tools.

---

## Open Source

All code is available on GitHub:
https://github.com/CreatorsEye/battery-reporter

You can:
- Read the source code
- Verify there's no data collection
- Modify it for your own use
- Build it yourself

---

## Contact Us

For privacy concerns or questions:

📧 **Email:** [Creatorseye@gmail.com](mailto:Creatorseye@gmail.com)  
🐛 **GitHub Issues:** [Open an issue](https://github.com/CreatorsEye/battery-reporter/issues)

We take privacy seriously and will respond to any concerns promptly.

---

## Transparency Report

| Year | Data Requests | Data Provided |
|------|---------------|---------------|
| 2024 | 0 | 0 |

We have never received any data requests because **we have no data to give.**

---

## Final Word

**Your battery data is yours. Your privacy is respected. No exceptions.**

— Creators Eye Team
