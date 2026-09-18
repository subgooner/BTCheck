# Basic Target Check Tool

Small python CLI tool for reconnaissance.

## About

This project was created as my first Python project for fun and practice. It can be used for test a target machine, for example on HackTheBox, TryHackMe etc. There are no any innovation functional or features. Overall, it's just a compilation of basic enumiration tools, I made it for my convenience. Do not take it serious.

## Features

- Ping host availability check rigth after program start
- Nmap service/version scan detection
- Optional DNS subdomain enumiration
- Custom wordlist support

## Reqirements

- Python3
- Nmap
- Gobuster

## Installation

Clone the repository:

```bash
git clone https://github.com/subgooner/BTCheck
cd BTCheck
```

## Run

python3 main.py

## Usage
The program will ask for:
- Target IP
- Domain (after nmap enumiration)
- Wordlist (after nmap enumiration)
````
Example:

Target: 10.10.10.10

Host reachable

Starting Nmap...
...

Domain: (n to skip): target.htb
Wordlist: (n to skip): /path/to/wordlist
````

## Disclaimer

This project is intended for authorized security testing, CTFs, labs and educational purposes only.

Do not use this tool against systems without permission.

