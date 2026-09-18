import subprocess

def ping(target):

    testping = subprocess.run(["ping", "-c", "1", target], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    return testping.returncode == 0


def runnmap(target):
    nmap = subprocess.run(["nmap", "-sV", target], capture_output=True, text=True)

    return nmap.stdout


def subdomains(domain, wordlst):
    sub = subprocess.run(
   [
            "gobuster",
            "dns",
            "--domain", domain,
            '--wordlist', wordlst
        ],
        capture_output=True,
        text=True
   )

    return sub.stdout

def main():
    target = input("Target: ").strip()

    if not ping(target):
        print("Host unreachable")
        return
    print("Host reachable\n")

    nmap_output = runnmap(target)

    if nmap_output is None:
        print("Nmap error")
        return

    print(nmap_output)

    domain = input("Domain: ").strip()
    wordlist = input("Wordlist: ").strip()

    if domain.lower() in ["n", "none"] or wordlist.lower() in ["n", "none"]:
        print("Subdomains skipped")
        return

    print(subdomains(domain, wordlist))

if __name__ == "__main__":
    main()