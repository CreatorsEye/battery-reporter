# CEBT – Python Version for Developers

For developers who want to modify the code or install via pip.

---

## Quick Start

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run directly
```bash
python cebt.py /S
```

### Install globally
```bash
pip install .
cebt /S
```

---

## Installation Options

### Option 1: Run without installing
```bash
python cebt.py /S
python cebt.py /R
python cebt.py /C
python cebt.py /L
python cebt.py /O "folder"
python cebt.py /H
```

### Option 2: Install with pip
```bash
pip install .
cebt /S
```

### Option 3: Editable install (for development)
```bash
pip install -e .
```

---

## Commands

| Command | Description |
|:---|:---|
| `cebt /S` | Start a new battery test |
| `cebt /R` | Show last test results |
| `cebt /C` | Compare all tests |
| `cebt /L` | Open last report in browser |
| `cebt /O "folder"` | Set output folder |
| `cebt /H` | Show help |

---

## Project Structure

```text
cebt.py              # Main script
requirements.txt     # Dependencies
setup.py            # For pip install
README.md           # This file
```

---

## Requirements

* Python 3.6 or higher
* Dependencies listed in `requirements.txt`

---

## Development

To contribute:

1. **Fork** the repository
2. **Clone** your fork
3. **Install** in editable mode:
   ```bash
   pip install -e .
   ```
4. **Make** your changes
5. **Test** with `python cebt.py /S`
6. **Submit** a pull request

---

## License

**MIT** – Free for everyone. Use, modify, and share.
