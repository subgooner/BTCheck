import subprocess


def ping():

    ip = input("Target IP: ").strip()

    testping = subprocess.run(["ping", "-c", "1", ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    if  testping.returncode == 0:
        print("Host is up")
    else:
        print("Host is down")


def nmap(command):
    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode != 0:
        return None

    return result.stdout

def gobust():
    print("""
    [1] DNS scan
    [2] URL scan  
    """)
    choice = input("Select: ")
    if choice == "1":
        domain = input("Domain to scan: ")
        wordlist = input("Wordlist: ")

        command = ["gobuster", "dns", "-d", domain, "-w", wordlist]

        print(f"\nCommand: {' '.join(command)}")
        confirm = input("Do you want to continue? [y/n]: ").strip().lower()

        if confirm in ("y", "", "yes"):
            result = subprocess.run(command, capture_output=True, text=True)

            print(result.stdout)

            if result.returncode != 0:
                print(result.stderr)
        else:
            print("Canceled")

    elif choice == "2":
        url = input("URL to scan: ")
        wordlist = input("Wordlist: ")

        command = ["gobuster", "dir", "-u", url, "-w", wordlist]

        print(f"\nCommand: {' '.join(command)}")
        confirm = input("Do you want to continue? [y/n]: ")

        if confirm in ("y", "", "yes"):
            result = subprocess.run(command, capture_output=True, text=True)

            print(result.stdout)

            if result.returncode != 0:
                print(result.stderr)
        else:
            print("Canceled")
    else:
        print("Canceled")


def ferox():
    url = input("URL to scan: ")
    wordlist = input("Wordlist: ")

    command = ["feroxbuster", "-u", url, "-w", wordlist]

    print(f"\nCommand: {' '.join(command)}")
    confirm = input("Do you want to continue? [y/n]: ")

    if confirm in ("y", "", "yes"):
        result = subprocess.run(command, capture_output=True, text=True)
        print(result.stdout)

        if result.returncode != 0:
            print(result.stderr)
    else:
        print("Canceled")

def ffuf():

    print("""
        [1] VHOST scan
        [2] URL scan  
        """)

    choice = input("Select: ")

    if choice == "1":
        url = input("URL to scan: ")
        wordlist = input("Wordlist: ")
        host = input("Host to scan (target.com): ").strip()

        command = ["ffuf", "-u", url, "-w", wordlist, "-H", f"Host: FUZZ.{host}"]

        print(f"\nCommand: {' '.join(command)}")
        confirm = input("Do you want to continue? [y/n]: ").strip().lower()

        if confirm in ("y", "", "yes"):
            result = subprocess.run(command, capture_output=True, text=True)

            print(result.stdout)

            if result.returncode != 0:
                print(result.stderr)
        else:
            print("Canceled")

    elif choice == "2":
        url = input("URL to scan (http://domain.com/FUZZ): ").strip()
        wordlist = input("Wordlist: ").strip()

        command = ["ffuf", "-u", url, "-w", wordlist]

        print(f"\nCommand: {' '.join(command)}")
        confirm = input("Do you want to continue? [y/n]: ")

        if confirm in ("y", "", "yes"):
            result = subprocess.run(command, capture_output=True, text=True)

            print(result.stdout)

            if result.returncode != 0:
                print(result.stderr)
        else:
            print("Canceled")
    else:
        print("Canceled")


def nmap_menu():

    scans = {
        "1": ["nmap"],
        "2": ["nmap", "-p-", "-A"]
    }

    while True:
        print("""
    ╔══════════════════════════════════════╗
    ║               NMAP SCAN              ║
    ╠══════════════════════════════════════╣
    ║    [1] Quick Scan                    ║
    ║    [2] Full Port Scan                ║
    ║    [3] Custom Scan                   ║
    ║    [0] Back                          ║
    ╚══════════════════════════════════════╝   
    """)

        choice = input("Select: ")

        if choice == "0":
            break
        if choice == "3":
            target = input("Target IP: ").strip()
            args = input("Arguments: ").strip().split()

            command = ["nmap"] + args + [target]

        elif choice in scans:
            target = input("Target IP: ").strip()

            command = scans[choice] + [target]

        else:
            print("Invalid option")
            continue

        print(f"\nCommand: {' '.join(command)}")

        confirm = input("Continue? [y/n] ").strip().lower()
        if confirm not in ["", "y", "yes"]:
            print("Scan cancelled")

            continue
        output = nmap(command)

        if output is None:
            print("Nmap error")

            continue

        print(output)


def web_menu():


    while True:
        print("""
    ╔══════════════════════════════════════╗
    ║             WEB ANALYSIS             ║
    ╠══════════════════════════════════════╣
    ║   [1] Gobuster                       ║
    ║   [2] feroxbuster                    ║
    ║   [3] FFUF                           ║
    ║   [0] Back                           ║
    ╚══════════════════════════════════════╝

    """)
        choice = input("Select: ").strip()
        if choice == "0":
            break
        elif choice == "1":
            gobust()
        elif choice == "2":
            ferox()
        elif choice == "3":
            ffuf()

        else:
            print("Invalid option")


def JTR():
    john_modes = {
        "1":"dictionary",
        "2":"incremental"

    }

    while True:
        print("""
    ╔══════════════════════════════════════╗
    ║          John The Ripper             ║
    ╠══════════════════════════════════════╣
    ║    [1] Dictionary attack             ║
    ║    [2] Incremental                   ║
    ║    [0] Back                          ║
    ╚══════════════════════════════════════╝ 
    
    """)

        choice = input("Select: ").strip()

        if choice == "0":
            break

        if choice not in john_modes:
            print("Invalid choice")
            return

        hash_file = input("Hash file: ").strip()

        if john_modes[choice] == "dictionary":
            wordlist = input("Wordlist: ").strip()

            command = ["john", f"--wordlist={wordlist}", hash_file]
        elif john_modes[choice] == "incremental":
            wordlist = input("Wordlist: ").strip()

            command = ["john", "--incremental", hash_file]

        print(f"\nCommand: {' '.join(command)}")

        confirm = input("Do you want to continue? [y/n]: ").strip().lower()

        if confirm in ("y", "", "yes"):
            result = subprocess.run(command, capture_output=True, text=True)
            print(result.stdout)

            if result.returncode != 0:
                print(result.stderr)

        else:
            print("Canceled")


def hashcat():

    hash_types = {
        "1": ("MD5", "0"),
        "2": ("SHA1", "100"),
        "3": ("SHA-256", "1400"),
        "4": ("NTML", "1000")


    }

    hashcat_modes = {
        "1": "dictionary",
        "2": "brute-force"

    }

    while True:
        print("""
    ╔══════════════════════════════════════╗
    ║              Hashcat                 ║
    ╠══════════════════════════════════════╣
    ║    [1] Dictionary attack             ║
    ║    [2] Brute-force / Mask            ║
    ║    [0] Back                          ║
    ╚══════════════════════════════════════╝ 

    """)

        choice = input("Select: ").strip()

        if choice == "0":
            break

        if choice not in hashcat_modes:
            print("Invalid choice")
            return

        print("""
        [1] MD5
        [2] SHA1
        [3] SHA-256
        [4] NTML
        """)

        hash_choice = input("Hash type: ").strip()

        if hash_choice not in hash_types:
            print("Invalid choice")
            return

        hash_name, hash_mode = hash_types[hash_choice]

        hash_file = input("Hash file: ").strip()

        if hashcat_modes[choice] == "dictionary":
            wordlist = input("Wordlist: ").strip()

            command = ["hashcat", "-m", hash_mode, "-a", "0", hash_file, wordlist]

        elif hashcat_modes[choice] == "brute-force":
            mask = input("Mask: ").strip()

            command = ["hashcat", "-m", hash_mode, "-a", "3", hash_file, mask]

        print(f"\nHash type: {hash_name}")
        print(f"\nCommand: {' '.join(command)}")

        confirm = input("Do you want to continue? [y/n]: ").strip().lower()

        if confirm in ("y", "", "yes"):
            result = subprocess.run(command, capture_output=True, text=True)
            print(result.stdout)

            if result.returncode != 0:
                print(result.stderr)

        else:
            print("Canceled")


def passwd_menu():
    while True:
        print("""
    ╔══════════════════════════════════════╗
    ║          PASSWORD ANALYSIS           ║
    ╠══════════════════════════════════════╣
    ║    [1] JohnTheRipper                 ║
    ║    [2] Hashcat                       ║
    ║    [0] Back                          ║ 
    ╚══════════════════════════════════════╝ 
    
    """)

        choice = input("Select: ").strip()
        if choice == "0":
            break
        elif choice == "1":
            JTR()
        elif choice == "2":
            hashcat()
        else:
            print("Invalid option")



def menu():

    while True:
        print("""
    ╔══════════════════════════════════════╗
    ║               BTCheck                ║
    ╠══════════════════════════════════════╣
    ║    [1] Nmap                          ║
    ║    [2] Web Analysis                  ║
    ║    [3] Password Analysis             ║
    ║    [4] Ping target                   ║
    ║    [0] Exit                          ║
    ╚══════════════════════════════════════╝
    
    """)

        choice = input("Select: ").strip()
        if choice == "1":
            nmap_menu()

        elif choice == "2":
            web_menu()

        elif choice == "3":
            passwd_menu()

        elif choice == "4":
            ping()

        elif choice == "0":
            print("Exiting")

            break
        else:
            print("Invalid option")


def main():

    menu()


if __name__ == "__main__":
    main()