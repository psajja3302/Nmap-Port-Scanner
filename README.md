# 🔍 Nmap Port Scanner

> Building on a [simple port scanner](https://github.com/pavansajja/Simple-Port-Scanner), this project incorporates the `nmap` module for deeper network reconnaissance — including service detection, protocol identification, and version fingerprinting.

---

## ⚠️ Legal Disclaimer

**This tool is intended for educational purposes and authorized network scanning only.**

Scanning networks or systems without explicit permission is **illegal and unethical** in most jurisdictions. Always ensure you have written authorization before scanning any network or host you do not personally own.

> I have tested this tool exclusively on my own private virtual network, isolated from my ISP, using a **Metasploitable 2.0** instance as the target.

📖 Read more: [https://nmap.org/book/legal-issues.html](https://nmap.org/book/legal-issues.html)

---

## 📋 Features

- Scans a user-specified IP address and port range
- Multi-threaded scanning (400 threads) for fast results
- Service and version detection via `-sV`
- Filter output: open ports only, or all ports
- Validates IP address format using regex
- Validates port range (0–65535)
- Clean, nmap-style formatted output

---

## 🛠️ Requirements

- macOS (tested) or Kali Linux
- Python 3.x
- [Homebrew](https://brew.sh) (macOS only)
- `nmap` binary
- `python-nmap` Python module

---

## ⚙️ Installation & Setup

### Step 1 — Install the nmap binary

On **macOS**, use Homebrew:
```bash
brew install nmap
```

On **Kali Linux**, nmap comes pre-installed. To verify:
```bash
nmap --version
```

---

### Step 2 — Set up a Python virtual environment in VSCode

It is strongly recommended to use a virtual environment to keep your dependencies isolated per project.

Open your project folder in VSCode, then open the integrated terminal (`Ctrl + `` ` ``) and run:

```bash
# Create the virtual environment
python3 -m venv .venv

# Activate it (you'll see (.venv) appear in your terminal prompt)
source .venv/bin/activate
```

---

### Step 3 — Install the python-nmap module

With your virtual environment active:
```bash
pip install python-nmap
```

Verify it works:
```bash
python3 -c "import nmap; print('nmap ready!')"
```

---

### Step 4 — Select the correct interpreter in VSCode

VSCode needs to know which Python interpreter to use so it can resolve the `nmap` module:

1. In your terminal (with `.venv` active), run:
   ```bash
   which python3
   ```
   This outputs something like:
   ```
   /Users/yourname/PythonProjects/NmapScanner/.venv/bin/python3
   ```

2. Open the Command Palette: `Cmd + Shift + P`
3. Search for **"Python: Select Interpreter"**
4. Click **"Enter interpreter path..."**
5. Paste the path from Step 1

> VSCode saves this interpreter choice per project folder — you won't need to repeat this step every time you open the project.

---

## 🚀 Usage

Run the scanner from your terminal:
```bash
python3 nmap_portscanner.py
```

You will be prompted to enter:
1. **Target IP address** — e.g. `192.168.1.10`
2. **Port range** — e.g. `20-80`
3. **Display mode** — `1` for open ports only, `2` for all ports

### Example Output

```
Scanning ports 20 – 30 on 192.168.1.10...

PORT       STATE        PROTOCOL   SERVICE         PRODUCT & VERSION
----------------------------------------------------------------------
21         open         tcp        ftp             vsftpd 2.3.4
22         open         tcp        ssh             OpenSSH 4.7p1
23         open         tcp        telnet          N/A

Scan complete. 3 open port(s) found. 8 closed/filtered port(s) found.
```
