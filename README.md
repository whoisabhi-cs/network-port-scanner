# Multithreaded Network Port & Service Scanner

## Overview
This project is a Python-based multithreaded TCP port scanner with service banner detection capability.

It performs basic network reconnaissance by identifying open ports and retrieving service information.

---

## Features
- Multithreaded TCP scanning
- Service banner detection
- Custom port range selection
- JSON output support
- Command-line interface
- Structured modular design

---

## Technologies Used
- Python 3
- Socket Programming
- Multithreading
- Argparse
- JSON

---

## Installation

Clone the repository or download the project.

Install dependencies (if any):

pip install -r requirements.txt

---

## Usage

Basic scan:

python -m scanner.port_scanner -t 127.0.0.1 -sp 1 -ep 1024

Save results:

python -m scanner.port_scanner -t 127.0.0.1 -sp 1 -ep 1024 -o results.json

---

## Example Output

[OPEN] Port 902 → 220 VMware Authentication Daemon Version 1.10

---

## Learning Outcomes
- Understanding TCP socket programming
- Multithreading implementation
- Service banner detection techniques
- Python modular project structuring
- Command-line tool development

---

## Disclaimer
This tool is intended for educational purposes only. 
Use only on networks you own or have permission to test.