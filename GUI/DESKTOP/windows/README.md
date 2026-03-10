# CEBT Desktop for Windows

Standalone Windows application for battery testing. No browser needed.

---

## 📥 Download

[⬇️ CEBT-GUI.exe](./CEBT-GUI.exe)

**Requirements:** Windows 10 or later (64-bit)

---

## 🚀 Quick Start

1. Download `CEBT-GUI.exe`
2. Double-click to run
3. Click "I Agree" (first time only)
4. Charge your laptop to 100%
5. Unplug the charger
6. Click START TEST
7. Keep the app open (you can minimize it)
8. Test stops automatically at 5%
9. Report saves to your chosen folder

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| **Standalone** | No browser needed – runs as native Windows app |
| **Wake Lock** | Prevents computer from sleeping during test |
| **5-minute logging** | Automatically records battery level every 5 minutes |
| **Auto-stop at 5%** | Protects battery from deep discharge |
| **Discharge chart** | Visual graph of battery drain after each test |
| **Test comparison** | Compare durations of your last 5 tests |
| **Dark mode** | Automatically matches your system theme |
| **Folder selection** | Pick where reports are saved |
| **Recovery** | If app closes accidentally, you can resume the test |
| **Privacy first** | All data stays on your device |

---

## 📸 Screenshots

*(Screenshots would be added here)*

---

## 📂 Default Output Folder

Reports are saved to: `Documents\CEBT-Reports\`

Example: `C:\Users\YourName\Documents\CEBT-Reports\`

You can change this in the app settings.

---

## ❓ Frequently Asked Questions

### Do I need to install anything?
No. Just download and run. The app is self-contained.

### Is it safe?
Yes. The app runs entirely on your device. No data is sent anywhere.

### Why does Windows Defender show a warning?
The app is not digitally signed. This is common for open-source tools. The executable is built from the same code as the HTML version.

To run:
1. Click "More info" in the Windows Defender dialog
2. Click "Run anyway"

### Can I use it on Windows 7/8?
Windows 10 or later is recommended. It may work on Windows 8 but is not tested.

### Where are reports saved?
Default: `Documents\CEBT-Reports\`. You can choose any folder when starting a test.

### Can I close the app during test?
No – the test stops if you close the app. However, it saves progress every minute and will ask to resume when you reopen.

---

## ⚠️ Troubleshooting

### App won't start
- Download the file again (may be corrupted)
- Right-click and select "Run as administrator"
- Check Windows Defender – it may have blocked it

### Antivirus warning
This is a false positive. The app is built from open-source code. Add it to your antivirus exceptions.

### Wake Lock not working
- Make sure you're running on battery power
- Check if your system allows apps to prevent sleep
- Try running as administrator

### Test won't start
- Unplug the charger
- Make sure battery is at least 95%
- Check if battery is detected

### Can't find saved reports
Default location: `Documents\CEBT-Reports\`
Check if you changed the folder during test setup.

---

## 🔧 Uninstall

Simply delete the `CEBT-GUI.exe` file. No registry entries, no leftovers.

---

## 📜 License

MIT – Free for everyone. Use, modify, and share.

---

## 👨‍💻 About Creators Eye

We build simple, privacy-focused tools that run entirely on your device.

📧 **Email:** [Creatorseye@gmail.com](mailto:Creatorseye@gmail.com)  
🐛 **GitHub Issues:** [Open an issue](https://github.com/CreatorsEye/battery-reporter/issues)
