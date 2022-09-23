import requests
import os
from colored import fg, attr

z = fg("#90EE90")
g = fg("#FF0000")
h = fg("#DDA0DD	")
reset = attr("reset")
clear = lambda: os.system('cls') if os.name == 'nt' else os.system('clear')

clear()

logo = f"""

        █████  ██████   ██████  ██    ██ ████████    ███    ███ ███████ 
       ██   ██ ██   ██ ██    ██ ██    ██    ██       ████  ████ ██      
       ███████ ██████  ██    ██ ██    ██    ██       ██ ████ ██ █████   
       ██   ██ ██   ██ ██    ██ ██    ██    ██       ██  ██  ██ ██      
       ██   ██ ██████   ██████   ██████     ██    ██ ██      ██ ███████ 
                                                                 
                    {h}https://about.me{reset} - Username Checker
                    {h}Credits{reset} - https://github.com/widths                                 

"""
print(logo)
input(f"Press enter when you're ready to check usernames from - {h}names.txt{reset}")


def check():
    for username in open("names.txt", "r").read().splitlines():
        r = requests.get(f"https://about.me/{username}")
        if r.status_code == 404:
            print(f"{z}https://about.me/{username}{reset} is avaliable ")
        else:
            print(f"{g}https://about.me/{username}{reset} is NOT avaliable")


check()
