import os
import requests
import webbrowser

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print("""
\x1b[38;5;1m    ██▓███   ██▀███   ▒█████  ▒██   ██▒▓██   ██▓
   ▓██░  ██▒▓██ ▒ ██▒▒██▒  ██▒▒▒ █ █ ▒░ ▒██  ██▒
   ▓██░ ██▓▒▓██ ░▄█ ▒▒██░  ██▒░░  █   ░  ▒██ ██░
   ▒██▄█▓▒ ▒▒██▀▀█▄  ▒██   ██░ ░ █ █ ▒   ░ ▐██▓░
   ▒██▒ ░  ░░██▓ ▒██▒░ ████▓▒░▒██▒ ▒██▒  ░ ██▒▓░
   ▒▓▒░ ░  ░░ ▒▓ ░▒▓░░ ▒░▒░▒░ ▒▒ ░ ░▓ ░   ██▒▒▒ 
   ░▒ ░       ░▒ ░ ▒░  ░ ▒ ▒░ ░░   ░▒ ░ ▓██ ░▒░ 
   ░░         ░░   ░ ░ ░ ░ ▒   ░    ░   ▒ ▒ ░░  
            ░         ░ ░   ░    ░   ░ ░     
                                     ░ ░     
    """)

def fetch_proxies(urls, filename):
    clear_screen()
    banner()
    print(f"Fetching proxies for {filename.replace('.txt', '').upper()}...\n")
    proxies = []
    for url in urls:
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                proxies.extend(response.text.strip().split('\n'))
                print(f"[+] Fetched from {url}")
            else:
                print(f"[-] Failed to fetch from {url}, Status Code: {response.status_code}")
        except Exception as e:
            print(f"[!] Error fetching {url}: {e}")
    
    with open(filename, 'w') as file:
        file.write('\n'.join(proxies))
    print(f"\n[✓] Saved {len(proxies)} proxies to {filename}\n")
    input("Press Enter to return to menu...")
    main()

def open_github():
    github_url = "https://github.com/Thuankobtcode"
    print(f"Opening GitHub page: {github_url}")
    webbrowser.open(github_url)

def main():
    clear_screen()
    banner()
    proxy_sources = {
        "http": {
            "filename": "http.txt",
            "urls": [
    "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
    "https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt",
    "https://raw.githubusercontent.com/zloi-user/hideip.me/main/https.txt",
    "https://raw.githubusercontent.com/BreakingTechFr/Proxy_Free/main/proxies/http.txt",
    "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/http.txt",
    "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/https.txt",
    "https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/protocols/http/data.txt",
    "https://yakumo.rei.my.id/HTTP",
    "https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt",
    "https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/https.txt",
    "https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http.txt",
    "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt",
    "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/https/https.txt",
    "https://sunny9577.github.io/proxy-scraper/generated/http_proxies.txt",
    "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt"
            ]
        },
        "socks5": {
            "filename": "socks5.txt",
            "urls": [
    "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all",
    "https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt",
    "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
    "https://raw.githubusercontent.com/BreakingTechFr/Proxy_Free/main/proxies/socks5.txt",
    "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/socks5.txt",
    "https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/protocols/http/socks5.txt",
    "https://yakumo.rei.my.id/SOCKS5",
    "https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt",
    "https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/socks5.txt",
    "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/socks5/socks5.txt",
    "https://sunny9577.github.io/proxy-scraper/generated/socks5_proxies.txt",
    "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt"
            ]
        },
        "socks4": {
            "filename": "socks4.txt",
            "urls": [
    "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=10000&country=all&ssl=all&anonymity=all",
    "https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt",
    "https://raw.githubusercontent.com/BreakingTechFr/Proxy_Free/main/proxies/socks4.txt",
    "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/socks4.txt",
    "https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/protocols/http/socks4.txt",
    "https://yakumo.rei.my.id/SOCKS4",
    "https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt",
    "https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/socks4.txt",
    "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/socks4/socks4.txt",
    "https://sunny9577.github.io/proxy-scraper/generated/socks4_proxies.txt",
    "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt"
            ]
        }
    }
    
    print("Select proxy mode:")
    print("1. HTTP")
    print("2. SOCKS4")
    print("3. SOCKS5")
    print("4. GITHUB")
    choice = input("Enter choice (1-4): ")
    
    modes = {"1": "http", "2": "socks4", "3": "socks5"}
    
    if choice in modes:
        mode = modes[choice]
        fetch_proxies(proxy_sources[mode]["urls"], proxy_sources[mode]["filename"])
    elif choice == "4":
        open_github()
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
