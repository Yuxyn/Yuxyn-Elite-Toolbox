import os, sys, subprocess, time, socket, base64, random

def setup():
    try:
        from colorama import Fore, Style, init
        import requests
    except ImportError:
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
def main():
    if input(f"{Fore.YELLOW}Giriş Anahtarı: ") != "levy123": return
    while True:
        banner()
        print(f"{Fore.CYAN}--- ANA MENÜ ---")
        print(f"{Fore.WHITE}[1] Wi-Fi Şifre Çözücü       [9] Sistem Bilgileri")
        print(f"{Fore.WHITE}[2] IP/Konum Sorgulama      [10] Görev Yöneticisi")
        print(f"{Fore.WHITE}[3] Hızlı Port Tarayıcı     [11] DNS Çözücü")
        print(f"{Fore.WHITE}[4] Ping Stress Test        [12] MAC Adresim")
        print(f"{Fore.WHITE}[5] Base64 Şifreleme        [13] Şifre Oluşturucu")
        print(f"{Fore.WHITE}[6] Base64 Çözücü           [14] Web Header Bilgisi")
        print(f"{Fore.WHITE}[7] Sistem Temizleyici      [15] GitHub Sayfası")
        print(f"{Fore.WHITE}[8] Yerel Ağ Tarayıcı       [0] Çıkış")
        
        cmd = input(f"\n{Fore.YELLOW}Yuxyn Seçim: ")
        
        if cmd == "1":
            try:
                data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="ignore").split('\n')
                profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
                for i in profiles:
                    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="ignore").split('\n')
                    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
                    print(f"{Fore.GREEN}Ağ: {i:<15} Şifre: {results[0] if results else 'Açık'}")
            except: print(f"{Fore.RED}Hata: Yönetici izni lazım!")
        
        elif cmd == "2":
            target = input("IP: ")
            res = requests.get(f"http://ip-api.com/json/{target}").json()
            print(f"{Fore.GREEN}Ülke: {res.get('country')} | Şehir: {res.get('city')}")
            
        elif cmd == "4":
            target = input("Hedef: ")
            try:
                while True: 
                    os.system(f"ping {target} -l 65500 -n 1 > nul")
                    print(f"{Fore.RED}Paket Gönderiliyor... {target}", end="\r")
            except KeyboardInterrupt: print("\nDurduruldu.")
            
        elif cmd == "7":
            print("Gereksiz dosyalar temizleniyor...")
            os.system("del /q /s %temp%\\*")
            print(f"{Fore.GREEN}Temizlik Bitti!")

        elif cmd == "13":
            chars = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*"
            print(f"Yeni Şifren: {''.join(random.sample(chars, 12))}")

        elif cmd == "15": os.system("start https://github.com/Yuxyn/Yuxyn-Elite-Toolbox")
        elif cmd == "0": break
        input(f"\n{Fore.RED}Menüye dönmek için Enter...")

if __name__ == "__main__":
    main()