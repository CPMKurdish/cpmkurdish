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

__CHANNEL_USERNAME__ = "Rickdev999"
__GROUP_USERNAME__ = "CPMCheatsChannel"
__BOT_RICK_NAME__ = "@CPMCHEATSBOT"
_CHEATS_NAME = "CPMCheats"


from pystyle import Colors as pyColors
from pystyle import Colorate as pyColorate
from pystyle import Center as pyCenter
from pystyle import System as pySystem

import pickle
import time


# Banner de boas-vindas em estilo negrito e centralizado
BANNER = r"""
                               𝗖𝗔𝗥 𝗣𝗔𝗥𝗞𝗜𝗡𝗚 𝗠𝗨𝗟𝗧𝗜𝗣𝗟𝗔𝗬𝗘𝗥⠀
                                      𝗖𝗣𝗠 𝗖𝗛𝗘𝗔𝗧𝗦
                               𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥: @𝗥𝗶𝗰𝗸𝗱𝗲𝘃𝟵𝟵𝟵
                               
                               
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
                "𝗛𝗲𝗹𝗹𝗼, 𝗪𝗲𝗹𝗰𝗼𝗺𝗲! 𝗣𝗹𝗲𝗮𝘀𝗲 𝗲𝗻𝘁𝗲𝗿 𝘆𝗼𝘂𝗿 𝗻𝗮𝗺𝗲 𝘁𝗼 𝗰𝗼𝗻𝘁𝗶𝗻𝘂𝗲: ",
            )
        ).strip()
        if user_name:
            save_user_name(user_name)
            return user_name
        print(
            pyColorate.Horizontal(
                pyColors.yellow_to_red, "𝗡𝗮𝗺𝗲 𝗰𝗮𝗻𝗻𝗼𝘁 𝗯𝗲 𝗲𝗺𝗽𝘁𝘆. 𝗣𝗹𝗲𝗮𝘀𝗲 𝘁𝗿𝘆 𝗮𝗴𝗮𝗶𝗻."
            )
        )


def show_welcome_message(user_name):
    print(
        pyColorate.Horizontal(
            pyColors.yellow_to_red,
            pyCenter.XCenter(
                f"𝗛𝗲𝗹𝗹𝗼 {user_name}, 𝗬𝗼𝘂𝗿 𝗻𝗮𝗺𝗲 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝗹𝗼𝗮𝗱𝗲𝗱 𝗳𝗿𝗼𝗺 𝘁𝗵𝗲 𝗳𝗶𝗹𝗲!"
            ),
        )
    )
    print(
        pyColorate.Horizontal(
            pyColors.yellow_to_red, pyCenter.XCenter("𝗧𝗵𝗮𝗻𝗸 𝘆𝗼𝘂 𝗳𝗼𝗿 𝘂𝘀𝗶𝗻𝗴 𝗰𝗽𝗺 𝗰𝗵𝗲𝗮𝘁𝘀!")
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

    input(pyColorate.Horizontal(pyColors.yellow_to_red, "𝗣𝗿𝗲𝘀𝘀 𝗘𝗻𝘁𝗲𝗿 𝘁𝗼 𝗰𝗼𝗻𝘁𝗶𝗻𝘂𝗲 ..."))


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
            if char != " ":
                color_index = int(
                    (
                        (x / (width - 1 if width > 1 else 1))
                        + (y / (height - 1 if height > 1 else 1))
                    )
                    * 0.5
                    * (len(colors) - 1)
                )
                color_index = min(
                    max(color_index, 0), len(colors) - 1
                )  # Ensure the index is within bounds
                style = Style(color=colors[color_index])
                colorful_text.append(char, style=style)
            else:
                colorful_text.append(char)
        colorful_text.append("\n")
    return colorful_text


import os


def banner(console):
    os.system("cls" if os.name == "nt" else "clear")

    brand_name = """
 ██████╗██████╗ ███╗   ███╗     ██████╗██╗  ██╗███████╗ █████╗ ████████╗███████╗
██╔════╝██╔══██╗████╗ ████║    ██╔════╝██║  ██║██╔════╝██╔══██╗╚══██╔══╝██╔════╝
██║     ██████╔╝██╔████╔██║    ██║     ███████║█████╗  ███████║   ██║   ███████╗
██║     ██╔═══╝ ██║╚██╔╝██║    ██║     ██╔══██║██╔══╝  ██╔══██║   ██║   ╚════██║
╚██████╗██║     ██║ ╚═╝ ██║    ╚██████╗██║  ██║███████╗██║  ██║   ██║   ███████║
 ╚═════╝╚═╝     ╚═╝     ╚═╝     ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝
                                                                                """

    colors = [
        "rgb(255,0,0)",  # Vermelho
        "rgb(255,51,0)",  # Vermelho-alaranjado
        "rgb(255,102,0)",  # Laranja
        "rgb(255,153,0)",  # Amarelo-alaranjado
        "rgb(255,204,0)",  # Amarelo
        "rgb(255,255,0)",  # Amarelo claro
    ]

    colorful_text = gradient_text(brand_name, colors)
    console.print(colorful_text)
    print(
        Colorate.Horizontal(
            Colors.yellow_to_red,
            "                   𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥 𝗔𝗡𝗗 𝗢𝗪𝗡𝗘𝗥:  𝗛𝗗 • 𝗥𝗜𝗖𝗞 𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥 ",
        )
    )
    print(
        Colorate.Horizontal(
            Colors.yellow_to_red,
            "╔═════════════════════════════[ 𝗜𝗠𝗣𝗢𝗥𝗧𝗔𝗡𝗧 ! ]═════════════════════════════╗",
        )
    )
    print(
        Colorate.Horizontal(
            Colors.yellow_to_red,
            "\t         𝗣𝗟𝗘𝗔𝗦𝗘 𝗟𝗢𝗚 𝗢𝗨𝗧 𝗢𝗙 𝗬𝗢𝗨𝗥 𝗔𝗖𝗖𝗢𝗨𝗡𝗧 𝗕𝗘𝗙𝗢𝗥𝗘 𝗨𝗦𝗜𝗡𝗚 𝗠𝗬 𝗧𝗢𝗢𝗟 ",
        )
    )
    print(
        Colorate.Horizontal(
            Colors.yellow_to_red,
            "    𝗜𝗙 𝗬𝗢𝗨 𝗦𝗛𝗔𝗥𝗘 𝗧𝗛𝗘 𝗞𝗘𝗬, 𝗬𝗢𝗨𝗥 𝗞𝗘𝗬 𝗪𝗜𝗟𝗟 𝗕𝗘 𝗕𝗟𝗢𝗖𝗞𝗘𝗗 𝗪𝗜𝗧𝗛𝗢𝗨𝗧 𝗡𝗢𝗧𝗜𝗖𝗘 ",
        )
    )
    print(
        Colorate.Horizontal(
            Colors.yellow_to_red,
            f" ‌           𝗧𝗘𝗟𝗘𝗚𝗥𝗔𝗠 : {__CHANNEL_USERNAME__} 𝗚𝗥𝗢𝗨𝗣 {__GROUP_USERNAME__}",
        )
    )
    print(
        Colorate.Horizontal(
            Colors.yellow_to_red,
            f"   𝗥𝗲𝗺𝗲𝗺𝗯𝗲𝗿: 𝗬𝗼𝘂 𝗻𝗲𝗲𝗱 𝗯𝗮𝗹𝗮𝗻𝗰𝗲 𝘁𝗼 𝘂𝘀𝗲 𝘁𝗵𝗲 𝘁𝗼𝗼𝗹. 𝗦𝗲𝗻𝗱 /𝘀𝘁𝗮𝗿𝘁 𝘁𝗼 {__BOT_RICK_NAME__}.",
        )
    )

    print(
        Colorate.Horizontal(
            Colors.yellow_to_red,
            "╚═════════════════════════════[. 𝗜𝗠𝗣𝗢𝗥𝗧𝗔𝗡𝗧 ! ]═════════════════════════════╝",
        )
    )

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
    start_rgb = tuple(int(start_color[i:i+2], 16) for i in (1, 3, 5))
    end_rgb = tuple(int(end_color[i:i+2], 16) for i in (1, 3, 5))
    interpolated_rgb = tuple(int(start + fraction * (end - start)) for start, end in zip(start_rgb, end_rgb))
    return "{:02x}{:02x}{:02x}".format(*interpolated_rgb)

def rainbow_gradient_string(customer_name):
    modified_string = ""
    num_chars = len(customer_name)
    start_color = "{:06x}".format(random.randint(0, 0xFFFFFF))
    end_color = "{:06x}".format(random.randint(0, 0xFFFFFF))
    for i, char in enumerate(customer_name):
        fraction = i / max(num_chars - 1, 1)
        interpolated_color = interpolate_color(start_color, end_color, fraction)
        modified_string += f'[{interpolated_color}]{char}'
    return modified_string


if __name__ == "__main__":
    console = Console()
    signal.signal(signal.SIGINT, signal_handler)
    while True:
        banner(console)
        acc_email = prompt_valid_value("[?] ACCOUNT EMAIL", "Email", password=False)
        acc_password = prompt_valid_value("[?] ACCOUNT PASSWORD", "Password", password=False)
        acc_access_key = prompt_valid_value("[?] ACCESS KEY", "Access Key", password=False)
        console.print("[%] TRYING TO LOGIN: ", end=None)
        cpm = CPMKurdish(acc_access_key)
        login_response = cpm.login(acc_email, acc_password)
        if login_response != 0:
            if login_response == 100:
                print(Colorate.Horizontal(Colors.rainbow, 'ACCOUNT NOT FOUND'))
                sleep(2)
                continue
            elif login_response == 101:
                print(Colorate.Horizontal(Colors.rainbow, 'WRONG PASSWORD'))
                sleep(2)
                continue
            elif login_response == 103:
                print(Colorate.Horizontal(Colors.rainbow, 'INVALID ACCESS KEY'))
                sleep(2)
                continue
            else:
                print(Colorate.Horizontal(Colors.rainbow, 'TRY AGAIN'))
                print(Colorate.Horizontal(Colors.rainbow, '! NOTE: MAKE SURE YOU FILLED OUT THE FIELDS'))
                sleep(2)
                continue
        else:
            print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
            sleep(2)
        while True:
            banner(console)
            load_player_data(cpm)
            load_key_data(cpm)
            load_client_details()
            choices = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39"]
            print(Colorate.Horizontal(Colors.rainbow, Center.XCenter(Box.DoubleCube( '                             𝑊𝐸𝐿𝐶𝑂𝑀𝐸 𝑇𝑂 𝑈𝑆𝐸 𝑀𝑌 𝑇𝑂𝑂𝐿\n\n             𝑁𝑂𝑇𝐸: 𝑇𝐻𝐸 𝑈𝑁𝐿𝐼𝑀𝐼𝑇𝐸𝐷 𝐵𝐴𝐿𝐴𝑁𝐶𝐸 𝑂𝑁𝐿𝑌 𝑊𝑂𝑅𝐾𝑆 𝐹𝑂𝑅 𝑂𝑁𝐸 𝑀𝑂𝑁𝑇𝐻\n\n\n01: Unlock Paid Cars           [3.500K] & 02: Increase Money            [1.000K]\n\n\n03: Unlock Coin Cars           [3.000K] & 04: Increase Coins            [3.000K]\n\n\n05: Unlock All Cars            [4.000K] & 06: King Rank                 [3.500K]\n\n\n07: Unlock all Cars Siren      [3.500K] & 08: Change ID                 [2.500K]\n\n\n09: Unlock w16 Engine          [3.000K] & 10: Change Name               [1..00K]\n\n\n11: Unlock All Horns           [3.000K] & 12: Change Name (Rainbow)     [1..00K]\n\n\n13: Unlock Disable Damage      [2.000K] & 14: Number Plates             [2.000K]\n\n\n15: Unlock Unlimited Fuel      [2.000K] & 16: Account Delete            [F.REE.]\n\n\n17: Unlock All Wheels          [2.500K] & 18: Account Register          [F.REE.]\n\n\n19: Unlock House 3             [2.500K] & 20: Delete Friends            [5..00K]\n\n\n21: Unlock Smoke               [2.000K] & 22: Change Race Wins          [7..00K]\n\n\n23: Change Race Loses          [7..00K] & 24: Custom Engine             [4.000K]\n\n\n25: remove car bumper (Car_ID) [2.000K] & 26: Speed Car Hack (Car_ID)   [1.500K]\n\n\n27: Speed All Cars Hack        [2.500K] & 28: Chrome All Cars           [3.500K]\n\n\n29: All Cars Max Milage        [2.000K] & 30: Clone Account             [5.000K]\n\n\n31: Unlock All Tuning          [1.000K] & 32: Steering Angle (Car_ID)   [1.500K]\n\n\n33: Unlock Equipaments Male    [3.000K] & 34: Unlock Equipaments Female [3.000K]\n\n\n35: Fake clan Dressing Male    [2.000K] & 36:﻿Fake clan Dressing Famale [2.000K]\n\n\n37: Remove Head Male           [2.500K] & 38: Remove Head Famale        [2.500K]\n\n\n                         𝑇𝐸𝐿𝐸𝐺𝑅𝐴𝑀 𝐵𝑂𝑇:- @CPMKurdishBot\n\n       𝑈𝑁𝐿𝐼𝑀𝐼𝑇𝐸𝐷 𝐵𝐴𝐿𝐴𝑁𝐶𝐸 𝐹𝑂R 𝐸𝑉𝐸𝑅𝑌 𝑃𝐸𝑅𝑆𝑂𝑁 𝑊𝐻𝑂 𝐴𝐷𝐷𝑆 100 𝑃𝐸𝑂𝑃𝐿𝐸 𝑇𝑂 𝑀𝑌 𝐺𝑅𝑂𝑈𝑃'))))
            print(Colorate.Horizontal(Colors.rainbow, Center.XCenter(Box.DoubleCube(  ' ➩{39}: GO TO ANOTHER ACCOUNT'))))
            print(Colorate.Horizontal(Colors.rainbow, Center.XCenter(Box.DoubleCube(  ' ➩{0}: Exit'))))
            print(Colorate.Horizontal(Colors.rainbow, '                               ─═══════════════[ ☆SERVICE☆ ]═══════════════─'))
            
            service = IntPrompt.ask(f"[bold]                                     [?] SELECT A SERVICE[red][1-{choices[-1]} or 0][/red][/bold]", choices=choices, show_choices=False)
            
            
            if service == 0: # Exit
                print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))



            elif service == 1: # Unlock All Paid Cars
                print(Colorate.Horizontal(Colors.rainbow, "[!] NOTE: THIS FUNCTION TAKES A WHILE TO COMPLETE, PLEASE DON'T CANCEL"))
                print(Colorate.Horizontal(Colors.rainbow, "[%] UNLOCKING ALL PAID CARS: "))
                if cpm.unlock_paid_cars():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue
                    
                    
                    
            elif service == 2: # Increase Money
                print(Colorate.Horizontal(Colors.rainbow, '[?] INSERT HOW MUCH MONEY DO YOU WANT'))
                amount = IntPrompt.ask("[?] AMOUNT")
                print(Colorate.Horizontal(Colors.rainbow, "[%] SAVING YOUR DATA:"))
                if amount > 0 and amount <= 999999999999999999999999999999:
                    if cpm.set_player_money(amount):
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
            elif service == 3: # Unlock All coins Cars
                print(Colorate.Horizontal(Colors.rainbow, "[!] NOTE: THIS FUNCTION TAKES A WHILE TO COMPLETE, PLEASE DON'T CANCEL"))
                print(Colorate.Horizontal(Colors.rainbow, "[%] UNLOCKING ALL COIN CARS: "))
                if cpm.unlock_coins_cars():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue              
                    
                          
                                      
            elif service == 4: # Increase Coins
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



            elif service == 5: # Unlock All Cars
                print(Colorate.Horizontal(Colors.rainbow, "[%] UNLOCKING ALL CARS: "))
                if cpm.unlock_all_cars():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue



            elif service == 6: # King Rank
                print(Colorate.Horizontal(Colors.rainbow, "[!] NOTE: IF THE KING RANK DOESN'T APPEAR IN GAME, CLOSE IT AND OPEN FEW TIMES"))
                print(Colorate.Horizontal(Colors.rainbow, "[!] NOTE: PLEASE DON'T DO KING RANK ON SAME ACCOUNT TWICE"))
                sleep(2)
                print(Colorate.Horizontal(Colors.rainbow, "[%] GIVING YOU A KING RANK: "))
                if cpm.set_player_rank():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)



                    continue



            elif service == 7: # Unlock All Cars Siren
                print(Colorate.Horizontal(Colors.rainbow, "[%] UNLOCKING ALL CARS SIREN: "))
                if cpm.unlock_all_cars_siren():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue



            elif service == 8: # Change ID
                print(Colorate.Horizontal(Colors.rainbow, '[?] ENTER YOUR NEW ID'))
                new_id = Prompt.ask("[red][?] ID[/red]")
                print(Colorate.Horizontal(Colors.rainbow, "[%] SAVING YOUR DATA: "))
                if len(new_id) >= 0 and len(new_id) <= 999999999 and (' ' in new_id) == False:
                    if cpm.set_player_localid(new_id.upper()):
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
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE USE VALID ID'))
                    sleep(2)
                    continue



            elif service == 9: # Unlock w16 Engine
                print(Colorate.Horizontal(Colors.rainbow, "[%] UNLOCKING W16 ENGINE: "))
                if cpm.unlock_w16():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue



            elif service == 10: # Change Name
                print(Colorate.Horizontal(Colors.rainbow, '[?] ENTER YOUR NEW NAME'))
                new_name = Prompt.ask("[red][?] NAME[/red]")
                print(Colorate.Horizontal(Colors.rainbow, "[%] SAVING YOUR DATA: "))
                if len(new_name) >= 0 and len(new_name) <= 999999999:
                    if cpm.set_player_name(new_name):
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



            elif service == 11: # Unlock All Horns
                print(Colorate.Horizontal(Colors.rainbow, "[%] UNLOCKING ALL HORNS: "))
                if cpm.unlock_horns():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue



            elif service == 12: # Change Name Rainbow
                print(Colorate.Horizontal(Colors.rainbow, '[?] ENTER YOUR NEW RAINBOW NAME'))
                new_name = Prompt.ask("[red][?] NAME[/red]")
                print(Colorate.Horizontal(Colors.rainbow, "[%] SAVING YOUR DATA: "))
                if len(new_name) >= 0 and len(new_name) <= 999999999:
                    if cpm.set_player_name(rainbow_gradient_string(new_name)):
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



            elif service == 13: # Disable Engine Damage
                print(Colorate.Horizontal(Colors.rainbow, "[%] UNLOCKING DISABLE DAMAGE: "))
                if cpm.disable_engine_damage():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue



            elif service == 14: # Number Plates
                print(Colorate.Horizontal(Colors.rainbow, "[%] GIVING YOU A NUMBER PLATES: "))
                if cpm.set_player_plates():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue



            elif service == 15: # Unlimited Fuel
                print(Colorate.Horizontal(Colors.rainbow, "[%] UNLOCKING UNLIMITED FUEL: "))
                if cpm.unlimited_fuel():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue



            elif service == 16: # Account Delete
                print(Colorate.Horizontal(Colors.rainbow, '[!] AFTER DELETING YOUR ACCOUNT THERE IS NO GOING BACK'))
                answ = Prompt.ask("[red][?] DO YOU WANT TO DELETE THIS ACCOUNT[/red]", choices=["y", "n"], default="n")
                if answ == "y":
                    cpm.delete()
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                else: continue



            elif service == 17: # Unlock Car Wheels
                print(Colorate.Horizontal(Colors.rainbow, "[%] UNLOCKING All WHEELS: "))
                if cpm.unlock_car_wheel():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue                                  



            elif service == 18: # Account Register
                print(Colorate.Horizontal(Colors.rainbow, '[!] REGISTRING NEW ACCOUNT'))
                acc2_email = prompt_valid_value("[red][?] ACCOUNT EMAIL[/red]", "Email", password=False)
                acc2_password = prompt_valid_value("[red][?] ACCOUNT PASSWORD[/red]", "Password", password=False)
                print(Colorate.Horizontal(Colors.rainbow, "[%] CREATING NEW ACCOUNT: "))
                status = cpm.register(acc2_email, acc2_password)
                if status == 0:
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, f'INFO: IN ORDER TO TWEAK THIS ACCOUNT WITH Ewan_Kurdish.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'YOU MOST SIGN-IN TO THE GAME USING THIS CCOUNT'))
                    sleep(2)
                    continue
                elif status == 105:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'THIS EMAIL IS ALREADY EXISTS'))
                    sleep(2)
                    continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue



            elif service == 19: # Unlock House 3
                print(Colorate.Horizontal(Colors.rainbow, "[%] UNLOCKING HOUSE 3:"))
                if cpm.unlock_houses():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue



            elif service == 20: # Delete Friends
                print(Colorate.Horizontal(Colors.rainbow, "[%] DELETING FRIENDS[/red]: "))
                if cpm.delete_player_friends():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue



            elif service == 21: # Unlock Smoke
                print(Colorate.Horizontal(Colors.rainbow, "[%] UNLOCKING SMOKE: "))
                if cpm.unlock_smoke():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue



            elif service == 22: # Change Races Wins
                print(Colorate.Horizontal(Colors.rainbow, '[!] Insert how much races you win.'))
                amount = IntPrompt.ask("[red][?] Amount[/red]")
                print(Colorate.Horizontal(Colors.rainbow, "[%] CHANGING YOUR DATA: "))
                if amount > 0 and amount <= 999999999999999999999999999999:
                    if cpm.set_player_wins(amount):
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



            elif service == 23: # Change Races Loses
                print(Colorate.Horizontal(Colors.rainbow, '[!] INSERT HOW MUCH RACES YOU LOSE'))
                amount = IntPrompt.ask("[red][?] AMOUNT[/red]")
                print(Colorate.Horizontal(Colors.rainbow, "[%] CHANGING YOUR DATA: "))
                if amount > 0 and amount <= 999999999999999999999999999999:
                    if cpm.set_player_loses(amount):
                        print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                        answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                        print(Colorate.Horizontal(Colors.rainbow, 'PLEASE USE VALID VALUES'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE USE VALID VALUES'))
                    sleep(2)
                    continue



            elif service == 24: # custom engine
                print(Colorate.Horizontal(Colors.rainbow, '[!] NOTE: ORIGINAL SPEED CAN NOT BE RESTORED'))            
                hp = IntPrompt.ask("[red][?] HP[/red]")                
                innerhp = IntPrompt.ask("[red][?] INNER HP[/red]")
                nm = IntPrompt.ask("[red][?] NM[/red]")
                innernm = IntPrompt.ask("[red][?] INNER NM[/red]")
                gearbox = IntPrompt.ask("[red][?] GEARBOX[/red]")                
                print(Colorate.Horizontal(Colors.rainbow, "[%] CUSTOM ENGINE: "))
                if cpm.custom_engine(hp, innerhp, nm, innernm, gearbox):
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue                    



            elif service == 25: # remove bumper
                print(Colorate.Horizontal(Colors.rainbow, '[!] ENTER CAR DETALIS'))
                car_id = IntPrompt.ask("[red][?] CAR ID[/red]")
                print(Colorate.Horizontal(Colors.rainbow, "[%] REMOVE ALL BUMPERS: "))
                if cpm.car_bumper(car_id):
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue



            elif service == 26: # Hack Car Speed (299hp)
                print(Colorate.Horizontal(Colors.rainbow, '[!] NOTE: ORIGINAL SPEED CAN NOT BE RESTORED'))
                print(Colorate.Horizontal(Colors.rainbow, '[!] ENTER CAR DETALIS'))
                car_id = IntPrompt.ask("[red][?] CAR ID[/red]")
                print(Colorate.Horizontal(Colors.rainbow, "[%] HACKING CAR SPEED: "))
                if cpm.hack_car_speed(car_id):
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue



            elif service == 27: # Hack All Car Speed 99hp
                print(Colorate.Horizontal(Colors.rainbow, '[!] NOTE: ORIGINAL SPEED CAN NOT BE RESTORED'))            
                print(Colorate.Horizontal(Colors.rainbow, "[%] HACKING ALL CARS SPEED: "))
                if cpm.hack_car_sexo():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue
                    
                    
                    
            elif service == 28: # Chrome All Cars
                print(Colorate.Horizontal(Colors.rainbow, '[!] CHROME'))            
                print(Colorate.Horizontal(Colors.rainbow, "[%] HACKING All CARS CHROME: "))
                if cpm.chrome_all_cars():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue               
                    
                    
                    
            elif service == 29: # ALL CARS MAX MILAGE
                print(Colorate.Horizontal(Colors.rainbow, '[!] NOTE: ORIGINAL MILAGE CAN NOT BE RESTORED'))            
                print(Colorate.Horizontal(Colors.rainbow, "[%] HACKING MILAGE: "))
                if cpm.hack_car_milage():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue                           
                    
                                                 
                                                                       
            elif service == 30: # Clone Account
                print(Colorate.Horizontal(Colors.rainbow, '[!] PLEASE ENTER ACCOUNT DETALIS'))
                to_email = prompt_valid_value("[red][?] ACCOUNT EMAIL[/red]", "Email", password=False)
                to_password = prompt_valid_value("[red][?] ACCOUNT PASSWORD[/red]", "Password", password=False)
                print(Colorate.Horizontal(Colors.rainbow, "[%] CLONING YOU ACCOUNT: "))
                if cpm.account_clone(to_email, to_password):
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE USE VALID VALUES'))
                    sleep(2)
                    continue
                    
                    
                    
            elif service == 31: # Unlock Tuning
                print(Colorate.Horizontal(Colors.rainbow, '[!] TUNING'))            
                print(Colorate.Horizontal(Colors.rainbow, "[%] UNLOCK ALL TUNING: "))
                if cpm.unlock_tuning():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue                                   
                    
                    
                    
            elif service == 32: # ANGLE
                print(Colorate.Horizontal(Colors.rainbow, '[!] ENTER CAR DETALIS'))
                car_id = IntPrompt.ask("[red][?] CAR ID[/red]")
                print(Colorate.Horizontal(Colors.rainbow, '[!] ENTER STEERING ANGLE'))
                custom = IntPrompt.ask("[red][?]﻿ENTER THE AMOUNT OF ANGLE YOU WANT[/red]")                
                print(Colorate.Horizontal(Colors.rainbow, "[%] HACKING CAR ANGLE: "))
                if cpm.max_max1(car_id, custom):
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue                    
                    
                    
                    
            elif service == 33: # Unlocking Equipaments Male
                print(Colorate.Horizontal(Colors.rainbow, ' %100'))
                print(Colorate.Horizontal(Colors.rainbow, "[%] Unlocking Equipaments Male: "))
                if cpm.unlock_equipments_male():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue                    
                    
                    
                    
            elif service == 34: # Unlocking Equipaments Female
                print(Colorate.Horizontal(Colors.rainbow, ' %100'))
                print(Colorate.Horizontal(Colors.rainbow, "[%] Unlocking Equipaments Female: "))
                if cpm.unlock_equipments_female():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue                    
                    
                    
                    
            elif service == 35: # Unlocking clan Equipaments Male
                print(Colorate.Horizontal(Colors.rainbow, ' %100'))            
                print(Colorate.Horizontal(Colors.rainbow, "[%] ﻿FAKE CLAN DRSSING MALE: "))
                if cpm.unlock_clan_equipments_male():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue                   
                    
                     
                       
            elif service == 36: # Unlocking clan Equipaments Female
                print(Colorate.Horizontal(Colors.rainbow, ' %100'))            
                print(Colorate.Horizontal(Colors.rainbow, "[%] FAKE CLAN DRSSING FEMALE: "))
                if cpm.unlock_clan_equipments_female():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue                                        
                    
                    
                    
            elif service == 37: # remove head Male
                print(Colorate.Horizontal(Colors.rainbow, ' %100'))            
                print(Colorate.Horizontal(Colors.rainbow, "[%] REMOVE HEAD MALE: "))
                if cpm.unlock_remove_face_male():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue                    
                    
                    
                    
            elif service == 38: # remove head Female
                print(Colorate.Horizontal(Colors.rainbow, ' %100'))            
                print(Colorate.Horizontal(Colors.rainbow, "[%] REMOVE HEAD FEMALE: "))
                if cpm.unlock_remove_face_female():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue                                                            
                    
                    
                    
            elif service == 39: # OPENING ANOTHER ACCOUNT
                print(Colorate.Horizontal(Colors.rainbow, '[!] PLEASE ENTER ACCOUNT DETALIS'))
                account_email = prompt_valid_value("[red][?] ACCOUNT EMAIL[/red]", "Email", password=False)
                to_password = prompt_valid_value("[red][?] ACCOUNT PASSWORD[/red]", "Password", password=False)
                print(Colorate.Horizontal(Colors.rainbow, "[%] OPENING ANOTHER ACCOUNT: "))
                if cpm.another_account(account_email, to_password):
                    print(Colorate.Horizontal(Colors.rainbow, 'ACCOUNT NOT FOUND'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    sleep(2)
                    continue                    
            else: continue
            break
        break
