import socket
import requests
import platform
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_help():
    print("""
Available Commands:
  myip       - Show your local IP address
  publicip   - Show your public IP and geo information
  lookup     - Find IP address details (Any IP)
  sysinfo    - Show system and OS information
  help       - Show this help message
  clear      - Clear the terminal screen
  exit       - Exit the program
""")

def show_intro():
    print("="*50)
    print("🔍 IP Info CLI Tool by Abdullah".center(50))
    print("="*50)
    print("This tool lets you:")
    print("- Find your local & public IP")
    print("- Get geo info about any IP")
    print("- View your system info")
    print("- And more")
    print("- Use 'help' to see all commands\n")
    print("="*50)

def get_local_ip():
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        print(f"🖥️  Local IP Address: {ip_address}")
    except Exception as e:
        print("❌ Error:", e)

def get_public_ip():
    try:
        res = requests.get("https://ipinfo.io/json").json()
        print("🌐 Public IP Info:")
        print(f"IP      : {res.get('ip')}")
        print(f"City    : {res.get('city')}")
        print(f"Region  : {res.get('region')}")
        print(f"Country : {res.get('country')}")
        print(f"Org     : {res.get('org')}")
        print(f"Loc     : {res.get('loc')}")
    except Exception as e:
        print("❌ Error:", e)

def lookup_ip_info():
    ip = input("🔎 Enter IP to lookup: ").strip()
    try:
        res = requests.get(f"https://ipinfo.io/{ip}/json").json()
        print("\n📄 IP Info:")
        for key, value in res.items():
            print(f"{key.capitalize():<10}: {value}")
    except Exception as e:
        print("❌ Error:", e)

def get_sys_info():
    print("💻 System Info:")
    print(f"OS         : {platform.system()}")
    print(f"OS Version : {platform.version()}")
    print(f"Machine    : {platform.machine()}")
    print(f"Processor  : {platform.processor()}")
    print(f"Node Name  : {platform.node()}")
    print(f"Platform   : {platform.platform()}")

# Entry Point
def main():
    clear_screen()
    show_intro()
    show_help()

    while True:
        cmd = input("\n🛠️  Command > ").lower().strip()

        if cmd == 'myip':
            get_local_ip()
        elif cmd == 'publicip':
            get_public_ip()
        elif cmd == 'lookup':
            lookup_ip_info()
        elif cmd == 'sysinfo':
            get_sys_info()
        elif cmd == 'help':
            show_help()
        elif cmd == 'clear':
            clear_screen()
            show_intro()
            show_help()
        elif cmd == 'exit':
            print("👋 Exiting... Stay safe!")
            break
        else:
            print("❌ Unknown command! Type 'help' to see available options.")

if __name__ == "__main__":
    main()
