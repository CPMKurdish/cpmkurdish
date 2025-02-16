import os
import signal
import sys
import random
from time import sleep
from datetime import datetime

# Bibliotecas de terceiros
import requests
from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from rich.text import Text
from rich.style import Style

# Bibliotecas de estilo (pystyle)
import pystyle
from pystyle import Colors, Colorate
from cpmkurdish import CPMKurdish

__CHANNEL_USERNAME__ = "cpmkurdish_channel"
__GROUP_USERNAME__ = "cpmkurdish_group"
__BOT_RICK_NAME__ = "@CPMKurdish"
_CHEATS_NAME = "CPMKurdish"


from pystyle import Colors as pyColors
from pystyle import Colorate as pyColorate
from pystyle import Center as pyCenter
from pystyle import Center
from pystyle import System as pySystem

import pickle
import time


BANNER = r"""
                               𝗖𝗔𝗥 𝗣𝗔𝗥𝗞𝗜𝗡𝗚 𝗠𝗨𝗟𝗧𝗜𝗣𝗟𝗔𝗬𝗘𝗥⠀
                                      𝗖𝗣𝗠 𝗞𝗨𝗥𝗗𝗜𝗦𝗛
                               𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥: @𝗘𝗪𝗔𝗡_𝗦𝗛𝗘𝗫_𝗔𝗟𝗜
                               
                               
⣀⣀⣀⣀⣠⣤⣤⣤⠶⠶⠶⢦⣤⣤⣤⣄⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣤⠤⠤⠤⢤⣤⣤⣤⣤⣄⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣟⠛⠿⢭⣛⣉⠉⠉⠉⠉⠉⠉⠙⢿⡁⠀⠀⠉⠉⠉⠉⠛⣦⠤⠖⠒⠚⠛⠛⠛⠛⠛⢓⣶⠶⠖⠚⠉⢙⣁⣭⠭⠿⠛⠛⠛⠻⢶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢽⣄⢀⣠⡴⠛⠉⠉⠉⠉⠻⡗⠚⢻⡇⠀⠀⠀⠀⠀⣠⡴⠋⠀⠀⠀⠀⠀⢀⣠⠴⠚⠉⠀⠤⢤⡶⠊⠉⠀⠹⡄⠀⠀⠀⠀⠀⠀⠉⠻⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠉⠉⠀⠀⠀⠀⢀⣤⣴⣾⣥⣶⡾⣷⣀⣀⣠⣴⣿⠥⠤⣄⣀⣀⣀⡤⠖⠉⠀⠀⠀⠀⠀⠀⡜⠀⠀⠀⠀⠀⢹⣄⣀⣀⣀⣀⣀⣀⣀⣀⣹⣿⣶⣶⣤⣤⣀⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣰⠟⠻⠯⠥⣄⣄⣿⠓⠛⡛⢉⣭⣤⣤⣤⠤⠴⠚⠛⠁⠀⠀⠀⠈⠉⠉⠉⠉⠙⠛⠉⠉⠉⠉⠉⠉⣿⡁⠀⠀⠀⠀⢀⣀⣀⣀⣀⣉⣧⣀⢉⡽⠛⠛⢳⣦⡄⠀
⠀⠀⠀⠀⢰⡿⣄⡀⠀⠀⠀⠀⢉⣹⡿⢻⣿⠿⣿⣇⡉⣑⣦⣀⣀⣀⡤⠤⠤⣤⣤⡶⠶⠶⠶⠷⠶⢾⣉⠉⠉⠉⠙⡏⠉⠉⠉⠉⠉⠉⠁⠀⠀⠈⢹⢻⣿⠇⠀⣴⣿⣿⣿⣿
⠀⠀⠀⢠⡿⠀⠀⠉⠉⠙⠒⣶⡟⢉⣿⡿⠁⠀⢸⣿⠋⠉⣿⠀⠀⠀⢀⡤⠞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠲⡄⠀⠸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡟⠀⢰⣿⣿⣿⣿⢻
⠀⠀⠀⢸⡷⣦⣀⡀⠀⠀⠘⢿⣧⠞⢫⣷⣄⣠⠏⣸⠀⠀⡏⠀⢀⡴⠋⠀⠀⠀⠀⠀⢀⣴⣶⣶⣶⡦⣄⡀⠀⠈⢦⠀⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡿⠀⠀⣿⣿⣿⣾⣿⣴
⠀⠀⠀⢸⣷⡇⠀⠉⠑⣶⠀⠀⠀⠀⠀⠉⠉⠀⠐⡇⠀⢸⡇⣠⠟⠀⠀⠀⠀⠀⣠⣾⣿⡟⢀⣽⣧⡹⣟⣷⡀⠀⠈⣧⠸⡄⠀⠀⠀⠀⢀⣀⣠⣼⣿⠃⠀⢀⡇⠻⣿⣿⠟⠛
⠀⠀⠀⢸⡿⢷⣄⡀⢀⡇⠀⣀⣀⣀⣀⣀⣀⠀⢀⠇⠀⠈⢻⡟⠲⢶⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⠟⢷⢸⣹⣷⠀⠀⠘⣆⣧⣠⢤⣶⣾⣿⣿⣷⣿⣿⠤⠴⠚⠉⠉⠉⠁⠀⠀
⠀⠀⠀⢸⣿⣦⣍⡛⠻⠃⡜⠉⠉⠀⠈⠉⢹⡆⢸⠀⠀⠀⠈⢧⡀⠀⠀⢀⡝⢉⣿⣿⣿⣿⣿⣅⡀⣸⢻⢿⣿⠀⠀⠀⢹⡿⢷⣾⡿⠿⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠻⣿⣿⢿⣿⣷⣶⣧⣄⣀⣀⠀⠀⢸⡇⢸⠀⠀⠀⠀⠀⠉⠑⠲⡞⠀⠀⣿⣿⣿⡿⠿⣿⣿⠇⣼⡾⣹⠀⠀⣀⠼⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠻⢶⣭⣛⣻⣿⣷⡾⢿⣿⣿⣿⣷⣿⡦⠤⣤⣤⣀⣀⣠⣼⡇⠀⠀⠹⣿⣿⣿⠀⡨⢏⣼⣿⣧⣧⠴⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⠻⢯⣉⠙⣷⣼⣿⣇⣳⣿⠈⢧⠀⠸⣄⡰⠋⠀⠀⣧⣄⡀⠀⠈⠻⠽⢯⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""


def show_banner():
    for line in BANNER.splitlines():
        if line.strip():
            print(pyColorate.Horizontal(pyColors.yellow_to_red, pyCenter.XCenter(line)))
            time.sleep(0.1)
    print("\n")


def get_user_name():
    if os.path.exists("user_data.pkl"):
        with open("user_data.pkl", "rb") as file:
            user_data = pickle.load(file)
        return user_data.get("name", "")
    return ""


def save_user_name(name):
    user_data = {"name": name}
    with open("user_data.pkl", "wb") as file:
        pickle.dump(user_data, file)


def prompt_user_name():
    while True:
        user_name = input(
            pyColorate.Horizontal(
                pyColors.yellow_to_red,
                "𝗛𝗘𝗟𝗟𝗢, 𝗪𝗘𝗟𝗖𝗢𝗠𝗘, 𝗣𝗟𝗘𝗔𝗦𝗘 𝗘𝗡𝗧𝗘𝗥 𝗬𝗢𝗨𝗥 𝗡𝗔𝗠𝗘 𝗧𝗢 𝗖𝗢𝗡𝗧𝗜𝗡𝗨𝗘: ",
            )
        ).strip()
        if user_name:
            save_user_name(user_name)
            return user_name
        print(
            pyColorate.Horizontal(
                pyColors.yellow_to_red, "𝗡𝗔𝗠𝗘 𝗖𝗔𝗡𝗡𝗢𝗧 𝗕𝗘 𝗘𝗠𝗣𝗧𝗬. 𝗣𝗟𝗘𝗔𝗦𝗘 𝗧𝗥𝗬 𝗔𝗚𝗔𝗜𝗡"
            )
        )


def show_welcome_message(user_name):
    print(
        pyColorate.Horizontal(
            pyColors.yellow_to_red,
            pyCenter.XCenter(
                f"𝗛𝗘𝗟𝗟𝗢 {user_name}, 𝗬𝗢𝗨𝗥 𝗡𝗔𝗠𝗘 𝗛𝗔𝗦 𝗕𝗘𝗘𝗡 𝗟𝗢𝗔𝗗𝗘𝗗 𝗙𝗥𝗢𝗠 𝗧𝗛𝗘 𝗙𝗜𝗟𝗘"
            ),
        )
    )
    print(
        pyColorate.Horizontal(
            pyColors.yellow_to_red, pyCenter.XCenter("𝗧𝗛𝗔𝗡𝗞 𝗬𝗢𝗨 𝗙𝗢𝗥 𝗨𝗦𝗜𝗡𝗚 𝗖𝗣𝗠𝗘𝘄𝗮𝗻 ")
        )
    )


def main():
    show_banner()

    user_name = get_user_name()

    if not user_name:
        user_name = prompt_user_name()

    pySystem.Clear()

    show_banner()

    show_welcome_message(user_name)

    input(pyColorate.Horizontal(pyColors.yellow_to_red, "𝗣𝗥𝗘𝗦𝗦 𝗘𝗡𝗧𝗘𝗥 𝗧𝗢 𝗖𝗢𝗡𝗧𝗜𝗡𝗨𝗘 ..."))


if __name__ == "__main__":
    main()


def signal_handler(sig, frame):
    print("\n Bye Bye...")
    sys.exit(0)


def gradient_text(text, colors):
    lines = text.splitlines()
    height = len(lines)
    width = max(len(line) for line in lines)
    colorful_text = Text()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != ' ':
                color_index = int(((x / (width - 1 if width > 1 else 1)) + (y / (height - 1 if height > 1 else 1))) * 0.5 * (len(colors) - 1))
                color_index = min(max(color_index, 0), len(colors) - 1)
                style = Style(color=colors[color_index])
                colorful_text.append(char, style=style)
            else:
                colorful_text.append(char)
        colorful_text.append("\n")
    return colorful_text


import os


def banner(console):
    os.system('cls' if os.name == 'nt' else 'clear')
    brand_name =  "                  ▄████▄   ██▓███   ███▄ ▄███▓▓█████  █     █░ ▄▄▄       ███▄    █ \n"
    brand_name += "                  ▒██▀ ▀█  ▓██░  ██▒▓██▒▀█▀ ██▒▓█   ▀ ▓█░ █ ░█░▒████▄     ██ ▀█   █ \n"
    brand_name += "                  ▒▓█    ▄ ▓██░ ██▓▒▓██    ▓██░▒███   ▒█░ █ ░█ ▒██  ▀█▄  ▓██  ▀█ ██▒\n"
    brand_name += "                  ▒▓▓▄ ▄██▒▒██▄█▓▒ ▒▒██    ▒██ ▒▓█  ▄ ░█░ █ ░█ ░██▄▄▄▄██ ▓██▒  ▐▌██▒\n"
    brand_name += "                  ▒ ▓███▀ ░▒██▒ ░  ░▒██▒   ░██▒░▒████▒░░██▒██▓  ▓█   ▓██▒▒██░   ▓██░\n"
    brand_name += "                  ░ ░▒ ▒  ░▒▓▒░ ░  ░░ ▒░   ░  ░░░ ▒░ ░░ ▓░▒ ▒   ▒▒   ▓▒█░░ ▒░   ▒ ▒ \n"
    colors = [
        "rgb(255,0,0)", "rgb(255,69,0)", "rgb(255,140,0)", "rgb(255,215,0)", "rgb(173,255,47)", 
        "rgb(0,255,0)", "rgb(0,255,255)", "rgb(0,191,255)", "rgb(0,0,255)", "rgb(139,0,255)",
        "rgb(255,0,255)"
    ]
    colorful_text = gradient_text(brand_name, colors)
    console.print(colorful_text)
    print(Colorate.Horizontal(Colors.rainbow, Center.XCenter( '─══════════════════════════════════════════☆☆═════════════════════════════════════════─')))
    
    print(Colorate.Horizontal(Colors.rainbow, Center.XCenter("𝐏𝐋𝐄𝐀𝐒𝐄 𝐋𝐎𝐆𝐎𝐔𝐓 𝐅𝐑𝐎𝐌 𝐂𝐏𝐌 𝐁𝐄𝐅𝐎𝐑𝐄 𝐔𝐒𝐈𝐍𝐆 𝐓𝐇𝐈𝐒 𝐓𝐎𝐎𝐋")))
    
    print(Colorate.Horizontal(Colors.rainbow, Center.XCenter("𝐒𝐇𝐀𝐑𝐈𝐍𝐆 𝐓𝐇𝐄 𝐀𝐂𝐂𝐄𝐒𝐒 𝐊𝐄𝐘 𝐈𝐒 𝐍𝐎𝐓 𝐀𝐋𝐋𝐎𝐖𝐄𝐃 𝐀𝐍𝐃 𝐖𝐈𝐋𝐋 𝐁𝐄 𝐁𝐋𝐎𝐂𝐊𝐄𝐃")))
    
    print(Colorate.Horizontal(Colors.rainbow, Center.XCenter(f" 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦: @{__CHANNEL_USERNAME__} 𝐎𝐫 @{__GROUP_USERNAME__}")))
    
    print(Colorate.Horizontal(Colors.rainbow, Center.XCenter('─════════════════════════════[ 𝖯𝖫𝖠𝖸𝖤𝖱 𝖣𝖤𝖳𝖠𝖨𝖫𝖲 ]════════════════════════════─')))


def load_player_data(cpm):
    response = cpm.get_player_data()
    if response.get('ok'):
        data = response.get('data')
        if 'floats' in data and 'localID' in data and 'money' in data and 'coin' in data:

            print(Colorate.Horizontal(Colors.rainbow, Center.XCenter(f'Name: {(data.get("Name") if "Name" in data else "UNDEFINED")} <> LocalID: {data.get("localID")} <> Money: {data.get("money")} <> Coins: {data.get("coin")}')))

        else:
            print(Colorate.Horizontal(Colors.rainbow, '! ERROR: new accounts most be signed-in to the game at least once !.'))
            exit(1)
    else:
        print(Colorate.Horizontal(Colors.rainbow, '! ERROR: seems like your login is not properly set !.'))
        exit(1)


def load_key_data(cpm):

    data = cpm.get_key_data()

    print(Colorate.Horizontal(Colors.rainbow, Center.XCenter('─══════════════════════[ 𝖠𝖢𝖢𝖤𝖲𝖲 𝖪𝖤𝖸 𝖣𝖤𝖳𝖠𝖨𝖫𝖲 ]══════════════════════─')))

    print(Colorate.Horizontal(Colors.yellow_to_red, f"Welcome {get_user_name()}"))

    print(Colorate.Horizontal(Colors.rainbow, Center.XCenter(f'Access Key: {data.get("access_key")} <> Telegram ID: {data.get("telegram_id")} <> Balance: {(data.get("coins") if not data.get("is_unlimited") else "Unlimited")}')))


def prompt_valid_value(content, tag, password=False):
    while True:
        value = Prompt.ask(content, password=password)
        if not value or value.isspace():
            print(Colorate.Horizontal(Colors.rainbow, f'{tag} CANNOT BE EMPTY OR JUST SPACES, PLEASE TRY AGAIN'))
        else:
            return value
            
def load_client_details():
    response = requests.get("http://ip-api.com/json")
    data = response.json()
    print(Colorate.Horizontal(Colors.rainbow, Center.XCenter('─═════════════════════[ 𝖫𝖮𝖢𝖠𝖳𝖨𝖮𝖭 ]═════════════════════─')))
    print(Colorate.Horizontal(Colors.rainbow, Center.XCenter(f'Country: {data.get("country")} <> Region: {data.get("regionName")} <> City: {data.get("city")}')))


def interpolate_color(start_color, end_color, fraction):
    start_rgb = tuple(int(start_color[i : i + 2], 16) for i in (1, 3, 5))
    end_rgb = tuple(int(end_color[i : i + 2], 16) for i in (1, 3, 5))
    interpolated_rgb = tuple(
        int(start + fraction * (end - start)) for start, end in zip(start_rgb, end_rgb)
    )
    return "{:02x}{:02x}{:02x}".format(*interpolated_rgb)


def rainbow_gradient_string(customer_name):
    modified_string = ""
    num_chars = len(customer_name)
    start_color = "{:06x}".format(random.randint(0, 0xFFFFFF))
    end_color = "{:06x}".format(random.randint(0, 0xFFFFFF))
    for i, char in enumerate(customer_name):
        fraction = i / max(num_chars - 1, 1)
        interpolated_color = interpolate_color(start_color, end_color, fraction)
        modified_string += f"[{interpolated_color}]{char}"
    return modified_string


if __name__ == "__main__":
    console = Console()
    signal.signal(signal.SIGINT, signal_handler)
    while True:
        banner(console)
        acc_email = prompt_valid_value(
            "[bold][?] Account Email[/bold]", "Email", password=False
        )
        acc_password = prompt_valid_value(
            "[bold][?] Account Password[/bold]", "Password", password=False
        )
        acc_access_key = prompt_valid_value(
            "[bold][?] Access Key[/bold]", "Access Key", password=False
        )
        console.print("[bold cyan][%] Trying to Login[/bold cyan]: ", end=None)
        cpm = CPMKurdish(acc_access_key)
        login_response = cpm.login(acc_email, acc_password)
        if login_response != 0:
            if login_response == 100:
                print(Colorate.Horizontal(Colors.yellow_to_red, "ACCOUNT NOT FOUND."))
                sleep(2)
                continue
            elif login_response == 101:
                print(Colorate.Horizontal(Colors.yellow_to_red, "WRONG PASSWORD."))
                sleep(2)
                continue
            elif login_response == 103:
                print(Colorate.Horizontal(Colors.yellow_to_red, "INVALID ACCESS KEY."))
                sleep(2)
                continue
            else:
                print(Colorate.Horizontal(Colors.yellow_to_red, "try again (✖)."))
                print(
                    Colorate.Horizontal(
                        Colors.yellow_to_red,
                        "! Note: make sure you filled out the fields !.",
                    )
                )
                sleep(2)
                continue
        else:
            print(Colorate.Horizontal(Colors.yellow_to_red, "Success (✓)."))
            sleep(2)
        while True:
            banner(console)
            load_player_data(cpm)
            load_key_data(cpm)
            load_client_details()
            choices = [
                "0",
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "10",
                "11",
                "12",
                "13",
                "14",
                "15",
                "16",
                "17",
                "18",
                "19",
                "20",
                "21",
                "22",
                "23",
            ]
            print(
                Colorate.Horizontal(
                    Colors.yellow_to_red, "→ {01}: 𝗜𝗻𝗰𝗿𝗲𝗮𝘀𝗲 𝗠𝗼𝗻𝗲𝘆 𝟭.𝟬𝟬𝟬$"
                )
            )
            print(
                Colorate.Horizontal(
                    Colors.yellow_to_red, "→ {02}: 𝗜𝗻𝗰𝗿𝗲𝗮𝘀𝗲 𝗖𝗼𝗶𝗻𝘀 𝟯.𝟱𝟬𝟬$"
                )
            )
            print(Colorate.Horizontal(Colors.yellow_to_red, "→ {03}: 𝗞𝗶𝗻𝗴 𝗥𝗮𝗻𝗸 𝟰.𝟬𝟬𝟬$"))
            print(Colorate.Horizontal(Colors.yellow_to_red, "→ {04}: 𝗖𝗵𝗮𝗻𝗴𝗲 𝗜𝗗 𝟯.𝟱𝟬𝟬$"))
            print(Colorate.Horizontal(Colors.yellow_to_red, "→ {05}: 𝗖𝗵𝗮𝗻𝗴𝗲 𝗡𝗮𝗺𝗲 𝟭𝟬𝟬$"))
            print(
                Colorate.Horizontal(
                    Colors.yellow_to_red, "→ {06}: 𝗖𝗵𝗮𝗻𝗴𝗲 𝗡𝗮𝗺𝗲 (𝗥𝗮𝗶𝗻𝗯𝗼𝘄) 𝟭𝟬𝟬$"
                )
            )
            print(
                Colorate.Horizontal(
                    Colors.yellow_to_red, "→ {07}: 𝗡𝘂𝗺𝗯𝗲𝗿 𝗣𝗹𝗮𝘁𝗲𝘀 𝟮.𝟬𝟬𝟬$"
                )
            )
            print(
                Colorate.Horizontal(Colors.yellow_to_red, "→ {08}: 𝗔𝗰𝗰𝗼𝘂𝗻𝘁 𝗗𝗲𝗹𝗲𝘁𝗲 𝗙𝗥𝗘𝗘")
            )
            print(
                Colorate.Horizontal(
                    Colors.yellow_to_red, "→ {09}: 𝗔𝗰𝗰𝗼𝘂𝗻𝘁 𝗥𝗲𝗴𝗶𝘀𝘁𝗲𝗿 𝗙𝗥𝗘𝗘"
                )
            )
            print(
                Colorate.Horizontal(Colors.yellow_to_red, "→ {10}: 𝗗𝗲𝗹𝗲𝘁𝗲 𝗙𝗿𝗶𝗲𝗻𝗱𝘀 𝟱𝟬𝟬$")
            )
            print(
                Colorate.Horizontal(
                    Colors.yellow_to_red, "→ {11}: 𝗨𝗻𝗹𝗼𝗰𝗸 𝗣𝗮𝗶𝗱 𝗖𝗮𝗿𝘀 𝟰.𝟬𝟬𝟬$"
                )
            )
            print(
                Colorate.Horizontal(
                    Colors.yellow_to_red, "→ {12}: 𝗨𝗻𝗹𝗼𝗰𝗸 𝗮𝗹𝗹 𝗖𝗮𝗿𝘀 𝟯.𝟬𝟬𝟬$"
                )
            )
            print(
                Colorate.Horizontal(
                    Colors.yellow_to_red, "→ {13}: 𝗨𝗻𝗹𝗼𝗰𝗸 𝗮𝗹𝗹 𝗖𝗮𝗿𝘀 𝗦𝗶𝗿𝗲𝗻 𝟮.𝟬𝟬𝟬$"
                )
            )
            print(
                Colorate.Horizontal(
                    Colors.yellow_to_red, "→ {14}: 𝗨𝗻𝗹𝗼𝗰𝗸 𝘄𝟭𝟲 𝗘𝗻𝗴𝗶𝗻𝗲 𝟯.𝟬𝟬𝟬$"
                )
            )
            print(
                Colorate.Horizontal(
                    Colors.yellow_to_red, "→ {15}: 𝗨𝗻𝗹𝗼𝗰𝗸 𝗔𝗹𝗹 𝗛𝗼𝗿𝗻𝘀 𝟯.𝟬𝟬𝟬$"
                )
            )
            print(
                Colorate.Horizontal(
                    Colors.yellow_to_red, "→ {16}: 𝗨𝗻𝗹𝗼𝗰𝗸 𝗗𝗶𝘀𝗮𝗯𝗹𝗲 𝗗𝗮𝗺𝗮𝗴𝗲 𝟮.𝟬𝟬𝟬$"
                )
            )
            print(
                Colorate.Horizontal(
                    Colors.yellow_to_red, "→ {17}: 𝗨𝗻𝗹𝗼𝗰𝗸 𝗨𝗻𝗹𝗶𝗺𝗶𝘁𝗲𝗱 𝗙𝘂𝗲𝗹 𝟮.𝟬𝟬𝟬$"
                )
            )
            print(
                Colorate.Horizontal(
                    Colors.yellow_to_red, "→ {18}: 𝗨𝗻𝗹𝗼𝗰𝗸 𝗛𝗼𝘂𝘀𝗲 𝟯 𝟯.𝟱𝟬𝟬$"
                )
            )
            print(
                Colorate.Horizontal(Colors.yellow_to_red, "→ {19}: 𝗨𝗻𝗹𝗼𝗰𝗸 𝗦𝗺𝗼𝗸𝗲 𝟮.𝟬𝟬𝟬$")
            )
            print(
                Colorate.Horizontal(
                    Colors.yellow_to_red, "→ {20}: 𝗖𝗵𝗮𝗻𝗴𝗲 𝗥𝗮𝗰𝗲 𝗪𝗶𝗻𝘀 𝟭.𝟬𝟬𝟬$"
                )
            )
            print(
                Colorate.Horizontal(
                    Colors.yellow_to_red, "→ {21}: 𝗖𝗵𝗮𝗻𝗴𝗲 𝗥𝗮𝗰𝗲 𝗟𝗼𝘀𝗲𝘀 𝟭.𝟬𝟬𝟬$"
                )
            )
            print(
                Colorate.Horizontal(
                    Colors.yellow_to_red, "→ {22}: 𝗦𝗽𝗲𝗲𝗱 𝗖𝗮𝗿 𝗛𝗮𝗰𝗸 𝟮𝟱𝟬𝟬$"
                )
            )
            print(
                Colorate.Horizontal(Colors.yellow_to_red, "→ {23}: 𝗖𝗹𝗼𝗻𝗲 𝗔𝗰𝗰𝗼𝗻𝘁 𝟱.𝟬𝟬𝟬$")
            )
            print(Colorate.Horizontal(Colors.yellow_to_red, "→ {0} : 𝗘𝘅𝗶𝘁"))

            print(
                Colorate.Horizontal(
                    Colors.yellow_to_red,
                    "╚═══════════════[ ☆ 𝗖𝗣𝗠 𝟭 𝗦𝗘𝗥𝗩𝗜𝗖𝗘𝗦☆ ]═══════════════╝",
                )
            )

            service = IntPrompt.ask(
                f"[bold][?] Select a Service [red][1-{choices[-1]} or 0][/red][/bold]",
                choices=choices,
                show_choices=False,
            )

            print(
                Colorate.Horizontal(
                    Colors.yellow_to_red,
                    "╚═══════════════[ ☆ 𝗖𝗣𝗠 𝟭 𝗦𝗘𝗥𝗩𝗜𝗖𝗘𝗦☆ ]═══════════════╝",
                )
            )

            if service == 0:  # Exit
                print(
                    Colorate.Horizontal(
                        Colors.yellow_to_red,
                        f"Thank You for using our tool, please join our telegram channel: @{__CHANNEL_USERNAME__}.",
                    )
                )
            elif service == 1:  # Increase Money
                print(
                    Colorate.Horizontal(
                        Colors.yellow_to_red, "[?] Insert how much money do you want."
                    )
                )
                amount = IntPrompt.ask("[?] Amount")
                console.print("[%] Saving your data: ", end=None)
                if amount > 0 and amount <= 999999999999999999999999999999:
                    if cpm.set_player_money(amount):
                        print(Colorate.Horizontal(Colors.yellow_to_red, "Success (✓)"))
                        print(
                            Colorate.Horizontal(
                                Colors.yellow_to_red,
                                "======================================",
                            )
                        )
                        answ = Prompt.ask(
                            "[?] Do You want to Exit ?", choices=["y", "n"], default="n"
                        )
                        if answ == "y":
                            print(
                                Colorate.Horizontal(
                                    Colors.yellow_to_red,
                                    f"Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.",
                                )
                            )
                        else:
                            continue
                    else:
                        print(Colorate.Horizontal(Colors.yellow_to_red, "FAILED."))
                        print(
                            Colorate.Horizontal(
                                Colors.yellow_to_red, "Please try again (✖)."
                            )
                        )
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.yellow_to_red, "FAILED."))
                    print(
                        Colorate.Horizontal(
                            Colors.yellow_to_red, "Please use valid values."
                        )
                    )
                    sleep(2)
                    continue
            elif service == 2:  # Increase Coins
                print(
                    Colorate.Horizontal(
                        Colors.yellow_to_red, "[?] Insert how much coins do you want."
                    )
                )
                amount = IntPrompt.ask("[?] Amount")
                console.print("[%] Saving your data: ", end=None)
                if amount > 0 and amount <= 999999999999999999999999999999:
                    if cpm.set_player_coins(amount):
                        print(Colorate.Horizontal(Colors.yellow_to_red, "Success (✓)"))
                        print(
                            Colorate.Horizontal(
                                Colors.yellow_to_red,
                                "======================================",
                            )
                        )
                        answ = Prompt.ask(
                            "[?] Do You want to Exit ?", choices=["y", "n"], default="n"
                        )
                        if answ == "y":
                            print(
                                Colorate.Horizontal(
                                    Colors.yellow_to_red,
                                    f"Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.",
                                )
                            )
                        else:
                            continue
                    else:
                        print(Colorate.Horizontal(Colors.yellow_to_red, "FAILED."))
                        print(
                            Colorate.Horizontal(
                                Colors.yellow_to_red, "Please try again (✖)."
                            )
                        )
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.yellow_to_red, "FAILED."))
                    print(
                        Colorate.Horizontal(
                            Colors.yellow_to_red, "Please use valid values."
                        )
                    )
                    sleep(2)
                    continue
            elif service == 3:  # King Rank
                console.print(
                    "[bold red][!] Note:[/bold red]: if the king rank doesn't appear in game, close it and open few times.",
                    end=None,
                )
                console.print(
                    "[bold red][!] Note:[/bold red]: please don't do King Rank on same account twice.",
                    end=None,
                )
                sleep(2)
                console.print("[%] Giving you a King Rank: ", end=None)
                if cpm.set_player_rank():
                    print(Colorate.Horizontal(Colors.yellow_to_red, "Success (✓)"))
                    print(
                        Colorate.Horizontal(
                            Colors.yellow_to_red,
                            "======================================",
                        )
                    )
                    answ = Prompt.ask(
                        "[?] Do You want to Exit ?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        print(
                            Colorate.Horizontal(
                                Colors.yellow_to_red,
                                f"Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.",
                            )
                        )
                    else:
                        continue
                else:
                    print(Colorate.Horizontal(Colors.yellow_to_red, "FAILED."))
                    print(
                        Colorate.Horizontal(
                            Colors.yellow_to_red, "Please try again (✖)."
                        )
                    )
                    sleep(2)
                    continue
            elif service == 4:  # Change ID
                print(
                    Colorate.Horizontal(Colors.yellow_to_red, "[?] Enter your new ID.")
                )
                new_id = Prompt.ask("[?] ID")
                console.print("[%] Saving your data: ", end=None)
                if (
                    len(new_id) >= 0
                    and len(new_id) <= 999999999
                    and (" " in new_id) == False
                ):
                    if cpm.set_player_localid(new_id.upper()):
                        print(Colorate.Horizontal(Colors.yellow_to_red, "Success (✓)"))
                        print(
                            Colorate.Horizontal(
                                Colors.yellow_to_red,
                                "======================================",
                            )
                        )
                        answ = Prompt.ask(
                            "[?] Do You want to Exit ?", choices=["y", "n"], default="n"
                        )
                        if answ == "y":
                            print(
                                Colorate.Horizontal(
                                    Colors.yellow_to_red,
                                    f"Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.",
                                )
                            )
                        else:
                            continue
                    else:
                        print(Colorate.Horizontal(Colors.yellow_to_red, "FAILED."))
                        print(
                            Colorate.Horizontal(
                                Colors.yellow_to_red, "Please try again (✖)."
                            )
                        )
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.yellow_to_red, "FAILED."))
                    print(
                        Colorate.Horizontal(
                            Colors.yellow_to_red, "Please use valid ID."
                        )
                    )
                    sleep(2)
                    continue
            elif service == 5:  # Change Name
                print(
                    Colorate.Horizontal(
                        Colors.yellow_to_red, "[?] Enter your new Name."
                    )
                )
                new_name = Prompt.ask("[?] Name")
                console.print("[%] Saving your data: ", end=None)
                if len(new_name) >= 0 and len(new_name) <= 999999999:
                    if cpm.set_player_name(new_name):
                        print(Colorate.Horizontal(Colors.yellow_to_red, "Success (✓)"))
                        print(
                            Colorate.Horizontal(
                                Colors.yellow_to_red,
                                "======================================",
                            )
                        )
                        answ = Prompt.ask(
                            "[?] Do You want to Exit ?", choices=["y", "n"], default="n"
                        )
                        if answ == "y":
                            print(
                                Colorate.Horizontal(
                                    Colors.yellow_to_red,
                                    f"Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.",
                                )
                            )
                        else:
                            continue
                    else:
                        print(Colorate.Horizontal(Colors.yellow_to_red, "FAILED."))
                        print(
                            Colorate.Horizontal(
                                Colors.yellow_to_red, "Please try again (✖)."
                            )
                        )
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.yellow_to_red, "FAILED."))
                    print(
                        Colorate.Horizontal(
                            Colors.yellow_to_red, "Please use valid values."
                        )
                    )
                    sleep(2)
                    continue
            elif service == 6:  # Change Name Rainbow
                print(
                    Colorate.Horizontal(
                        Colors.yellow_to_red, "[?] Enter your new Rainbow Name."
                    )
                )
                new_name = Prompt.ask("[?] Name")
                console.print("[%] Saving your data: ", end=None)
                if len(new_name) >= 0 and len(new_name) <= 999999999:
                    if cpm.set_player_name(rainbow_gradient_string(new_name)):
                        print(Colorate.Horizontal(Colors.yellow_to_red, "Success (✓)"))
                        print(
                            Colorate.Horizontal(
                                Colors.yellow_to_red,
                                "======================================",
                            )
                        )
                        answ = Prompt.ask(
                            "[?] Do You want to Exit ?", choices=["y", "n"], default="n"
                        )
                        if answ == "y":
                            print(
                                Colorate.Horizontal(
                                    Colors.yellow_to_red,
                                    f"Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.",
                                )
                            )
                        else:
                            continue
                    else:
                        print(Colorate.Horizontal(Colors.yellow_to_red, "FAILED."))
                        print(
                            Colorate.Horizontal(
                                Colors.yellow_to_red, "Please try again (✖)."
                            )
                        )
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.yellow_to_red, "FAILED."))
                    print(
                        Colorate.Horizontal(
                            Colors.yellow_to_red, "Please use valid values."
                        )
                    )
                    sleep(2)
                    continue
            elif service == 7:  # Number Plates
                console.print("[%] Giving you a Number Plates: ", end=None)
                if cpm.set_player_plates():
                    print(Colorate.Horizontal(Colors.yellow_to_red, "Success (✓)"))
                    print(
                        Colorate.Horizontal(
                            Colors.yellow_to_red,
                            "======================================",
                        )
                    )
                    answ = Prompt.ask(
                        "[?] Do You want to Exit ?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        print(
                            Colorate.Horizontal(
                                Colors.yellow_to_red,
                                f"Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.",
                            )
                        )
                    else:
                        continue
                else:
                    print(Colorate.Horizontal(Colors.yellow_to_red, "FAILED."))
                    print(
                        Colorate.Horizontal(
                            Colors.yellow_to_red, "Please try again (✖)."
                        )
                    )
                    sleep(2)
                    continue
            elif service == 8:  # Account Delete
                print(
                    Colorate.Horizontal(
                        Colors.yellow_to_red,
                        "[!] After deleting your account there is no going back !!.",
                    )
                )
                answ = Prompt.ask(
                    "[?] Do You want to Delete this Account ?!",
                    choices=["y", "n"],
                    default="n",
                )
                if answ == "y":
                    cpm.delete()
                    print(Colorate.Horizontal(Colors.yellow_to_red, "Success (✓)"))
                    print(
                        Colorate.Horizontal(
                            Colors.yellow_to_red,
                            "======================================",
                        )
                    )
                    print(
                        Colorate.Horizontal(
                            Colors.yellow_to_red,
                            f"Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.",
                        )
                    )
                else:
                    continue
            elif service == 9:  # Account Register
                print(
                    Colorate.Horizontal(
                        Colors.yellow_to_red, "[!] Registring new Account."
                    )
                )
                acc2_email = prompt_valid_value(
                    "[?] Account Email", "Email", password=False
                )
                acc2_password = prompt_valid_value(
                    "[?] Account Password", "Password", password=False
                )
                console.print("[%] Creating new Account: ", end=None)
                status = cpm.register(acc2_email, acc2_password)
                if status == 0:
                    print(Colorate.Horizontal(Colors.yellow_to_red, "Success (✓)"))
                    print(
                        Colorate.Horizontal(
                            Colors.yellow_to_red,
                            "======================================",
                        )
                    )
                    print(
                        Colorate.Horizontal(
                            Colors.yellow_to_red,
                            f"INFO: In order to tweak this account with Ewan_Kurdish.",
                        )
                    )
                    print(
                        Colorate.Horizontal(
                            Colors.yellow_to_red,
                            "you most sign-in to the game using this account.",
                        )
                    )
                    sleep(2)
                    continue
                elif status == 105:
                    print(Colorate.Horizontal(Colors.yellow_to_red, "FAILED."))
                    print(
                        Colorate.Horizontal(
                            Colors.yellow_to_red, "This email is already exists !."
                        )
                    )
                    sleep(2)
                    continue
                else:
                    print(Colorate.Horizontal(Colors.yellow_to_red, "FAILED."))
                    print(
                        Colorate.Horizontal(
                            Colors.yellow_to_red, "Please try again (✖)."
                        )
                    )
                    sleep(2)
                    continue
            elif service == 10:  # Delete Friends
                console.print("[%] Deleting your Friends: ", end=None)
                if cpm.delete_player_friends():
                    print(Colorate.Horizontal(Colors.yellow_to_red, "Success (✓)"))
                    print(
                        Colorate.Horizontal(
                            Colors.yellow_to_red,
                            "======================================",
                        )
                    )
                    answ = Prompt.ask(
                        "[?] Do You want to Exit ?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        print(
                            Colorate.Horizontal(
                                Colors.yellow_to_red,
                                f"Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.",
                            )
                        )
                    else:
                        continue
                else:
                    print(Colorate.Horizontal(Colors.yellow_to_red, "FAILED."))
                    print(
                        Colorate.Horizontal(
                            Colors.yellow_to_red, "Please try again (✖)."
                        )
                    )
                    sleep(2)
                    continue
            elif service == 11:  # Unlock All Paid Cars
                console.print(
                    "[!] Note: this function takes a while to complete, please don't cancel.",
                    end=None,
                )
                console.print("[%] Unlocking All Paid Cars: ", end=None)
                if cpm.unlock_paid_cars():
                    print(Colorate.Horizontal(Colors.yellow_to_red, "Success (✓)"))
                    print(
                        Colorate.Horizontal(
                            Colors.yellow_to_red,
                            "======================================",
                        )
                    )
                    answ = Prompt.ask(
                        "[?] Do You want to Exit ?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        print(
                            Colorate.Horizontal(
                                Colors.yellow_to_red,
                                f"Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.",
                            )
                        )
                    else:
                        continue
                else:
                    print(Colorate.Horizontal(Colors.yellow_to_red, "FAILED."))
                    print(
                        Colorate.Horizontal(
                            Colors.yellow_to_red, "Please try again (✖)."
                        )
                    )
                    sleep(2)
                    continue
            elif service == 12:  # Unlock All Cars
                console.print("[%] Unlocking All Cars: ", end=None)
                if cpm.unlock_all_cars():
                    print(Colorate.Horizontal(Colors.yellow_to_red, "Success (✓)"))
                    print(
                        Colorate.Horizontal(
                            Colors.yellow_to_red,
                            "======================================",
                        )
                    )
                    answ = Prompt.ask(
                        "[?] Do You want to Exit ?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        print(
                            Colorate.Horizontal(
                                Colors.yellow_to_red,
                                f"Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.",
                            )
                        )
                    else:
                        continue
                else:
                    print(Colorate.Horizontal(Colors.yellow_to_red, "FAILED."))
                    print(
                        Colorate.Horizontal(
                            Colors.yellow_to_red, "Please try again (✖)."
                        )
                    )
                    sleep(2)
                    continue
            elif service == 13:  # Unlock All Cars Siren
                console.print("[%] Unlocking All Cars Siren: ", end=None)
                if cpm.unlock_all_cars_siren():
                    print(Colorate.Horizontal(Colors.yellow_to_red, "Success (✓)"))
                    print(
                        Colorate.Horizontal(
                            Colors.yellow_to_red,
                            "======================================",
                        )
                    )
                    answ = Prompt.ask(
                        "[?] Do You want to Exit ?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        print(
                            Colorate.Horizontal(
                                Colors.yellow_to_red,
                                f"Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.",
                            )
                        )
                    else:
                        continue
                else:
                    print(Colorate.Horizontal(Colors.yellow_to_red, "FAILED."))
                    print(
                        Colorate.Horizontal(
                            Colors.yellow_to_red, "Please try again (✖)."
                        )
                    )
                    sleep(2)
                    continue
            elif service == 14:  # Unlock w16 Engine
                console.print("[%] Unlocking w16 Engine: ", end=None)
                if cpm.unlock_w16():
                    print(Colorate.Horizontal(Colors.yellow_to_red, "Success (✓)"))
                    print(
                        Colorate.Horizontal(
                            Colors.yellow_to_red,
                            "======================================",
                        )
                    )
                    answ = Prompt.ask(
                        "[?] Do You want to Exit ?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        print(
                            Colorate.Horizontal(
                                Colors.yellow_to_red,
                                f"Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.",
                            )
                        )
                    else:
                        continue
                else:
                    print(Colorate.Horizontal(Colors.yellow_to_red, "FAILED."))
                    print(
                        Colorate.Horizontal(
                            Colors.yellow_to_red, "Please try again (✖)."
                        )
                    )
                    sleep(2)
                    continue
            elif service == 15:  # Unlock All Horns
                console.print("[%] Unlocking All Horns: ", end=None)
                if cpm.unlock_horns():
                    print(Colorate.Horizontal(Colors.yellow_to_red, "Success (✓)"))
                    print(
                        Colorate.Horizontal(
                            Colors.yellow_to_red,
                            "======================================",
                        )
                    )
                    answ = Prompt.ask(
                        "[?] Do You want to Exit ?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        print(
                            Colorate.Horizontal(
                                Colors.yellow_to_red,
                                f"Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.",
                            )
                        )
                    else:
                        continue
                else:
                    print(Colorate.Horizontal(Colors.yellow_to_red, "FAILED."))
                    print(
                        Colorate.Horizontal(
                            Colors.yellow_to_red, "Please try again (✖)."
                        )
                    )
                    sleep(2)
                    continue
            elif service == 16:  # Disable Engine Damage
                console.print("[%] Unlocking Disable Damage: ", end=None)
                if cpm.disable_engine_damage():
                    print(Colorate.Horizontal(Colors.yellow_to_red, "Success (✓)"))
                    print(
                        Colorate.Horizontal(
                            Colors.yellow_to_red,
                            "======================================",
                        )
                    )
                    answ = Prompt.ask(
                        "[?] Do You want to Exit ?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        print(
                            Colorate.Horizontal(
                                Colors.yellow_to_red,
                                f"Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.",
                            )
                        )
                    else:
                        continue
                else:
                    print(Colorate.Horizontal(Colors.yellow_to_red, "FAILED."))
                    print(
                        Colorate.Horizontal(
                            Colors.yellow_to_red, "Please try again (✖)."
                        )
                    )
                    sleep(2)
                    continue
            elif service == 17:  # Unlimited Fuel
                console.print("[%] Unlocking Unlimited Fuel: ", end=None)
                if cpm.unlimited_fuel():
                    print(Colorate.Horizontal(Colors.yellow_to_red, "Success (✓)"))
                    print(
                        Colorate.Horizontal(
                            Colors.yellow_to_red,
                            "======================================",
                        )
                    )
                    answ = Prompt.ask(
                        "[?] Do You want to Exit ?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        print(
                            Colorate.Horizontal(
                                Colors.yellow_to_red,
                                f"Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.",
                            )
                        )
                    else:
                        continue
                else:
                    print(Colorate.Horizontal(Colors.yellow_to_red, "FAILED."))
                    print(
                        Colorate.Horizontal(
                            Colors.yellow_to_red, "Please try again (✖)."
                        )
                    )
                    sleep(2)
                    continue
            elif service == 18:  # Unlock House 3
                console.print("[%] Unlocking House 3: ", end=None)
                if cpm.unlock_houses():
                    print(Colorate.Horizontal(Colors.yellow_to_red, "Success (✓)"))
                    print(
                        Colorate.Horizontal(
                            Colors.yellow_to_red,
                            "======================================",
                        )
                    )
                    answ = Prompt.ask(
                        "[?] Do You want to Exit ?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        print(
                            Colorate.Horizontal(
                                Colors.yellow_to_red,
                                f"Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.",
                            )
                        )
                    else:
                        continue
                else:
                    print(Colorate.Horizontal(Colors.yellow_to_red, "FAILED."))
                    print(
                        Colorate.Horizontal(
                            Colors.yellow_to_red, "Please try again (✖)."
                        )
                    )
                    sleep(2)
                    continue
            elif service == 19:  # Unlock Smoke
                console.print("[%] Unlocking Smoke: ", end=None)
                if cpm.unlock_smoke():
                    print(Colorate.Horizontal(Colors.yellow_to_red, "Success (✓)"))
                    print(
                        Colorate.Horizontal(
                            Colors.yellow_to_red,
                            "======================================",
                        )
                    )
                    answ = Prompt.ask(
                        "[?] Do You want to Exit ?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        print(
                            Colorate.Horizontal(
                                Colors.yellow_to_red,
                                f"Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.",
                            )
                        )
                    else:
                        continue
                else:
                    print(Colorate.Horizontal(Colors.yellow_to_red, "FAILED."))
                    print(
                        Colorate.Horizontal(
                            Colors.yellow_to_red, "Please try again (✖)."
                        )
                    )
                    sleep(2)
                    continue
            elif service == 20:  # Change Races Wins
                print(
                    Colorate.Horizontal(
                        Colors.yellow_to_red, "[!] Insert how much races you win."
                    )
                )
                amount = IntPrompt.ask("[?] Amount")
                console.print("[%] Changing your data: ", end=None)
                if amount > 0 and amount <= 999999999999999999999999999999:
                    if cpm.set_player_wins(amount):
                        print(Colorate.Horizontal(Colors.yellow_to_red, "Success (✓)"))
                        print(
                            Colorate.Horizontal(
                                Colors.yellow_to_red,
                                "======================================",
                            )
                        )
                        answ = Prompt.ask(
                            "[?] Do You want to Exit ?", choices=["y", "n"], default="n"
                        )
                        if answ == "y":
                            print(
                                Colorate.Horizontal(
                                    Colors.yellow_to_red,
                                    f"Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.",
                                )
                            )
                        else:
                            continue
                    else:
                        print(Colorate.Horizontal(Colors.yellow_to_red, "FAILED."))
                        print(
                            Colorate.Horizontal(
                                Colors.yellow_to_red, "Please try again (✖)."
                            )
                        )
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.yellow_to_red, "FAILED."))
                    print(
                        Colorate.Horizontal(
                            Colors.yellow_to_red, "[!] Please use valid values."
                        )
                    )
                    sleep(2)
                    continue
            elif service == 21:  # Change Races Loses
                print(
                    Colorate.Horizontal(
                        Colors.yellow_to_red, "[!] Insert how much races you lose."
                    )
                )
                amount = IntPrompt.ask("[?] Amount")
                console.print("[%] Changing your data: ", end=None)
                if amount > 0 and amount <= 999999999999999999999999999999:
                    if cpm.set_player_loses(amount):
                        print(Colorate.Horizontal(Colors.yellow_to_red, "Success (✓)"))
                        print(
                            Colorate.Horizontal(
                                Colors.yellow_to_red,
                                "======================================",
                            )
                        )
                        answ = Prompt.ask(
                            "[?] Do You want to Exit ?", choices=["y", "n"], default="n"
                        )
                        if answ == "y":
                            print(
                                Colorate.Horizontal(
                                    Colors.yellow_to_red,
                                    f"Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.",
                                )
                            )
                        else:
                            continue
                    else:
                        print(Colorate.Horizontal(Colors.yellow_to_red, "FAILED."))
                        print(
                            Colorate.Horizontal(
                                Colors.yellow_to_red, "[!] Please use valid values."
                            )
                        )
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.yellow_to_red, "FAILED."))
                    print(
                        Colorate.Horizontal(
                            Colors.yellow_to_red, "[!] Please use valid values."
                        )
                    )
                    sleep(2)
                    continue
            elif service == 22:  # Hack Car Speed (299hp)
                console.print(
                    "[bold yellow][!] Note[/bold yellow]: original speed can not be restored !."
                )
                console.print("[bold cyan][!] Enter Car Details.[/bold cyan]")
                car_id = IntPrompt.ask("[bold][?] Car ID[/bold]")
                console.print(
                    "[bold cyan][%] Hacking Car Speed[/bold cyan]: ", end=None
                )
                if cpm.hack_car_speed(car_id):
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    console.print("==================================")
                    answ = Prompt.ask(
                        "[bold cyan][?] Do You want to Exit ?[/bold cyan]",
                        choices=["y", "n"],
                        default="n",
                    )
                    if answ == "y":
                        console.print(
                            "[bold yellow][!] Thank You for using our tool.[/bold yellow]."
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED (✘)[/bold red]")
                    console.print("[bold yellow][!] Please try again.[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 23:  # Clone Account
                print(
                    Colorate.Horizontal(
                        Colors.yellow_to_red, "[!] Please Enter Account Detalis."
                    )
                )
                to_email = prompt_valid_value(
                    "[?] Account Email", "Email", password=False
                )
                to_password = prompt_valid_value(
                    "[?] Account Password", "Password", password=False
                )
                console.print("[%] Cloning your account: ", end=None)
                if cpm.account_clone(to_email, to_password):
                    print(Colorate.Horizontal(Colors.yellow_to_red, "Success (✓)"))
                    print(
                        Colorate.Horizontal(
                            Colors.yellow_to_red,
                            "======================================",
                        )
                    )
                    answ = Prompt.ask(
                        "[?] Do You want to Exit ?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        print(
                            Colorate.Horizontal(
                                Colors.yellow_to_red,
                                f"Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.",
                            )
                        )
                    else:
                        continue
                else:
                    print(Colorate.Horizontal(Colors.yellow_to_red, "FAILED."))
                    print(
                        Colorate.Horizontal(
                            Colors.yellow_to_red, "[!] Please use valid values."
                        )
                    )
                    sleep(2)
                    continue
            else:
                continue
            break
        break
