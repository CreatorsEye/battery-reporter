# 🖥️ Creators Eye – Browser Battery Reporter

The simplest way to test your laptop battery. One HTML file, no installation.

---

## 📥 Download
[⬇️ Click here to download battery-reporter.html](./battery-reporter.html)  
*(right-click → "Save link as")*

---

## 🚀 Quick Start
1. **Open the file** in Chrome, Edge, Firefox, or Safari.
2. **First time only**: Click "I Agree" to accept the terms.
3. **Charge your laptop** to 100%.
4. **Unplug the charger**.
5. Click **START TEST**.
6. **Use your laptop normally** (keep this tab open – you can minimize it).
7. The test **stops automatically** when battery reaches **5%** (protects your battery).
8. A report is saved to your chosen folder (or Downloads as a ZIP file).

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| **Universal** | Works in Chrome, Edge, Firefox, Safari |
| **Wake Lock** | Prevents your computer from sleeping during the test (audio fallback for Firefox) |
| **5‑minute logging** | Automatically records battery level every 5 minutes |
| **Auto‑stop at 5%** | Protects battery from deep discharge |
| **Discharge chart** | Visual graph of battery drain after each test |
| **Test comparison** | Compare durations of your last 5 tests |
| **Dark mode** | Automatically matches your system theme |
| **Folder selection** | Pick a folder for reports (Chrome/Edge) – falls back to ZIP for all browsers |
| **Recovery** | If the tab closes accidentally, you can resume the test |
| **Privacy first** | All data stays on your device – nothing is uploaded |

---

## 📸 Screenshots

### Main Interface
*(Place screenshot named `browser-main.png` in this folder)*  
![Main Interface](./screenshots/browser-main.png)

### Test Running
*(Place screenshot named `browser-test.png` in this folder)*  
![Test Running](./screenshots/browser-test.png)

### Final Report with Chart
*(Place screenshot named `browser-report.png` in this folder)*  
![Report](./screenshots/browser-report.png)

---

## ❓ Frequently Asked Questions

**Q: Does it work in Firefox?**  
A: Yes! Firefox is fully supported. Folder selection is not available, so reports are saved as ZIP files – which contain the same information.

**Q: Will my computer sleep during the test?**  
A: No – the tool uses Wake Lock (native in Chrome/Edge, audio fallback in Firefox) to keep your system awake while the test runs.

**Q: Where are the reports saved?**  
A: If you're using Chrome/Edge and you pick a folder, reports go there. Otherwise, a ZIP file is downloaded to your Downloads folder. The ZIP contains both the final report and the full 5‑minute log.

**Q: Can I close the browser tab during the test?**  
A: No – the test stops if the tab is closed. However, the tool saves progress every minute, so when you reopen it you'll be asked if you want to resume.

**Q: Why does it stop at 5% instead of 0%?**  
A: Deep discharging lithium‑ion batteries (below 5%) can permanently damage them. Stopping at 5% is a safety feature to prolong your battery's life.

---

## ⚠️ Troubleshooting

| Problem | Solution |
|---------|----------|
| **Battery percentage not showing** | Use Chrome, Edge, or Firefox latest version. If the problem persists, your browser may not support the Battery API. |
| **Wake Lock inactive** | In Firefox, Wake Lock is simulated with silent audio – it still works. In Chrome/Edge, make sure you're on a secure connection (localhost or HTTPS). |
| **Folder picker doesn't open** | Your browser doesn't support the File System Access API. The tool will automatically save reports as ZIP files – perfectly fine. |
| **"Using ZIP fallback" warning in Chrome/Edge** | The folder you previously selected is no longer accessible (deleted, moved, or permissions lost). Click the location bar and pick a new folder. |
| **Test interrupted** | Reopen the tool – it will ask if you want to resume from the last saved state. |

---

## 👨‍💻 About Creators Eye
This tool is part of the Creators Eye collection – simple, privacy-focused tools that run entirely on your device.  
No data collection. No tracking. Just tools that work.

📧 **Email:** [Creatorseye@gmail.com](mailto:Creatorseye@gmail.com)

---

## 📜 License
MIT – Free for everyone. Use, modify, and share.
