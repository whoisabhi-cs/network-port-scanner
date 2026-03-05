0# 🔍 Multithreaded Port Scanner

A Python-based multithreaded port scanner that scans open ports on a target system quickly and efficiently.  
This tool is designed for learning networking fundamentals and basic cybersecurity reconnaissance.

---

## 🚀 Features

- ✅ Fast multithreaded port scanning
- ✅ Detects open ports on a target host
- ✅ Banner grabbing for service identification
- ✅ CLI-based tool
- ✅ Clean terminal output
- ✅ Beginner-friendly Python implementation

---

## 📂 Project Structure

```
port_scanner/
│
├── scanner/
│   ├── port_scanner.py
│   └── banner_grab.py
│
├── requirements.txt
└── README.md
```

---

## 🛠 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/whoisabhi-cs/network-port-scanner.git
cd port-scanner
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶ Usage

Run the scanner using:

```bash
python -m scanner.port_scanner
```

Example output:

```
Scanning target: 127.0.0.1

[OPEN] Port 135
[OPEN] Port 445
[OPEN] Port 902
[OPEN] Port 912

Service Info:
220 VMware Authentication Daemon Version 1.10
```

---

## 🔍 What This Tool Does

### 1️⃣ Port Scanning

The scanner attempts to connect to ports on the target system and identifies which ports are open.

### 2️⃣ Banner Grabbing

When an open port is found, the tool tries to retrieve service information from that port.

Example:

```
220 VMware Authentication Daemon Version 1.10
```

This helps identify the service running on that port.

---

## ⚡ Multithreading

To increase scanning speed, the scanner uses multithreading so multiple ports can be scanned simultaneously.

This significantly reduces scanning time compared to sequential scanning.

---

## 📡 Common Ports Detected

Examples of services associated with common ports:

| Port | Service |
|-----|--------|
| 21 | FTP |
| 22 | SSH |
| 25 | SMTP |
| 80 | HTTP |
| 443 | HTTPS |
| 445 | SMB |
| 3306 | MySQL |

---

## ⚠ Disclaimer

This tool is intended strictly for:

- Educational purposes
- Learning cybersecurity concepts
- Authorized testing environments

Do **NOT** use this tool on systems without permission.

---

## 👨‍💻 Author

Abhishek Sharma  
BCA Student | Cyber Security Enthusiast  
Passionate about cybersecurity, networking, and ethical hacking.
