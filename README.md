# Basic Target Check Tool

Small python CLI tool for reconnaissance.

## About

This project was created as my first Python project for fun and practice. It can be used for test a target machine, for example on HackTheBox, TryHackMe etc. There are no any innovation functional or features. Overall, it's just a compilation of basic enumeration tools, I made it for my convenience. Do not take it serious.

## Features

### Network

- Ping target
- Nmap scanning
    - Quick scan
    - Full port scan
    - Custom Nmap arguments
### Web Analysis

- Gobuster
    - DNS enumeration
    - Directory enumeration

- Feroxbuster

- FFUF
    - Virtual host fuzzing
    - URL fuzzing

### Password Analysis

- John The Ripper
    - Dictionary mode
    - Incremental mode

- Hashcat
    - Dictionary mode
    - Brute-force
    - Hash type selection

## Requirements

BTCheck is designed to run on Linux.

- Kali Linux (optional)
- Python3
- Nmap
- Gobuster
- Hashcat
- JohnTheRipper
- FFUF
- Feroxbuster

## Installation

Clone the repository:

```bash
git clone https://github.com/subgooner/BTCheck
cd BTCheck
```

## Run

python3 main.py

## Usage
After program start main menu will open:
````
    ╔══════════════════════════════════════╗
    ║               BTCheck                ║
    ╠══════════════════════════════════════╣
    ║    [1] Nmap                          ║
    ║    [2] Web Analysis                  ║
    ║    [3] Password Analysis             ║
    ║    [4] Ping target                   ║
    ║    [0] Exit                          ║
    ╚══════════════════════════════════════╝
````

By typing numbers user can chose option.

Also, some tools can ask other options. 
For example, in FFUF menu, after choosing option program asks for:
````
URL to scan (http://domain.com/FUZZ):
Wordlist:
````
Different tools asks different options


## Disclaimer

This project is intended for authorized security testing, CTFs, labs and educational purposes only.

Do not use this tool against systems without permission.

