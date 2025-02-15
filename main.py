import time, datetime, os, sys, random 
x = datetime.datetime.now()
colors = ['\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;34m', '\033[1;35m', '\033[1;36m']
W = '\033[0m'

from pystyle import Box
import random
import requests
from time import sleep
import os, signal, sys
from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from rich.text import Text
from rich.style import Style
import pystyle
from pystyle import Colors, Colorate
from pystyle import Center
import datetime



from cpmkurdish import CPMKurdish

__CHANNEL_USERNAME__ = "cpmkurdish_channel"
__GROUP_USERNAME__   = "cpmkurdish_group"

os.system("clear")

def clr():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')


def banner():
    clr()
    logo = """                                                  
      ███████   ██                                           
      ██▒▒▒▒▒   ██      ██                                        
      ██        ██      ▒▒                 ██      ██           
      ███████   ██      ██ ███████ ██   ██ ▒▒██  ██▒▒          
      ▒▒▒▒▒██   ██      ██ ██▒▒▒██ ██   ██   ▒▒██▒▒                
           ██   ██      ██ ██   ██ ██   ██   ██▒▒██              
      ███████   ███████ ██ ██   ██ ███████ ██▒▒  ▒▒██                         
      ▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒ ▒▒ ▒▒   ▒▒ ▒▒▒▒▒▒▒ ▒▒      ▒▒                  
                                         """
    print(random.choice(colors) + logo + W)
    print("\n")
def start():
    clr()
    banner()
    print("Tool started at\033[91;107m %s \033[0m " % x.strftime("%X"))
    time.sleep(3)
    print("██████████████████████████████████████████████████████████████")
    print("██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██")
    print("██            Coded by github.com/HACK3RY2J                 ██")
    print("██   Youtube : https://www.youtube.com/c/PandaHackers       ██")
    print("██  Telegram : https://telegram.me/HACK3RY2J                ██")
    print("██████████████████████████████████████████████████████████████")
    print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
    print()
    print()
    print("\033[92m  1. Kali Linux ")
    print("  2. Parrot ")
    print("  3. Arch")
    print("  4. Kali Nethunter ")
    print("  5. Backbox")
    print("  6. Alpine")
    print("  7. Opensuse-tumbelweed ")
    print("  8. Black Arch")
    print("  9. Opensuse-leap ")
    print(" 10. Ubuntu")
    print(" 11. Debian ")
    print(" 12. Fedora ")
    print(" 13. Centos \033[0m ")
    op = input("Choose your desired Linux : ")
    if op == "1":
        print("\033[91m Installing Kali... \033[0m")
        os.system("cd")
        time.sleep(1.5)
        os.system(
            "apt install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Kali/kali.sh && bash kali.sh")
            
            
    elif op == "2":
        print(Colorate.Horizontal(Colors.rainbow, '[?] INSERT HOW MUCH COINS DO YOU WANT'))
        amount = IntPrompt.ask("[red][?] AMOUNT[/red]")
        print(Colorate.Horizontal(Colors.rainbow, "[%] SAVING YOUR DATA: "))
        if amount > 0 and amount <= 999999999999999999999999999999:
            if cpm.set_player_coins(amount):
                print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))   
                answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                else: continue
            else:
                print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                sleep(2)
                continue
        else:
            print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
            print(Colorate.Horizontal(Colors.rainbow, 'PLEASE USE VALID VALUES'))
            sleep(2)



            continue
                
                
    elif op == "3":
        print("\033[91m Installing Arch... \033[0m ")
        os.system("cd")
        time.sleep(1.5)
        os.system(
            "apt install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Arch/armhf/arch.sh && bash arch.sh ")
    elif op == "4":
        print("\033[91m Installing Kali Nethunter... \033[0m")
        os.system("cd")
        time.sleep(1.5)
        os.system(
            "apt install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Nethunter/nethunter.sh && bash nethunter.sh")
    elif op == "5":
        print("\033[91m Installing Blackbox.. \033[0m")
        os.system("cd")
        time.sleep(1.5)
        os.system(
            "apt install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/BackBox/backbox.sh && bash backbox.sh")
    elif op == "6":
        print("\033[91m Installing Alpine... \033[0m")
        os.system("cd")
        time.sleep(1.5)
        os.system(
            "apy install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Alpine/alpine.sh && bash alpine.sh")
    elif op == "7":
        print("\033[91m Installing Tumbelweed... \033[0m")
        os.system("cd")
        time.sleep(1.5)
        os.system(
            "apt install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/openSUSE/Tumbleweed/opensuse-tumbleweed.sh && bash opensuse-tumbleweed.sh")
    elif op == "8":
        print("\033[91m Installing Black Arch... \033[0m")
        os.system("cd")
        time.sleep(1.5)
        os.system(
            "pacman-key --init && pacman-key --populate archlinuxarm && pacman -Sy --noconfirm curl && curl -O https://blackarch.org/strap.sh && chmod +x strap.sh && ./strap.sh")
    elif op == "9":
        print("\033[91m Installing opensuse-leap... \033[0m ")
        os.system("cd")
        time.sleep(1.5)
        os.system(
            "apt install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/openSUSE/Leap/opensuse-leap.sh && bash opensuse-leap.sh")
    elif op == "10":
        print("\033[91m Installing Ubuntu...\033[0m")
        os.sytem("cd")
        time.sleep(1.5)
        os.system(
            "apt install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Ubuntu/ubuntu.sh && bash ubuntu.sh")
    elif op == "11":
        print("\033[91m Installing Debian... \033[0m ")
        os.system("cd")
        time.sleep(1.5)
        o9s.system(
            "apt install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Debian/debian.sh && bash debian.sh")
    elif op == "12":
        print("\033[91m Installing Fedora... \033[0m ")
        os.system("cd")
        time.sleep(1.5)
        os.system(
            "apt install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Fedora/fedora.sh && bash fedora.sh")
    elif op == "13":
        print("\033[91m Installing Centos... \033[0m ")
        os.system("cd")
        time.sleep(1.5)
        os.system(
            "apt install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/CentOS/centos.sh && bash centos.sh")
    else:
        print(" Enter a valid option... ")
        
start()
