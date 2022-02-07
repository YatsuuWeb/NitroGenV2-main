from os import name, mkdir, system
from os.path import isdir
from random import choice
from pycenter import center, makebox
from terminaltables import DoubleTable
from art import text2art, FONT_NAMES
from pystyle import Colorate, Colors
import requests
import random, string

def clear():
    system("cls" if name == 'nt' else "clear")

if name == 'nt':
    system("title The NitroGen & mode 160, 40")




colors = [col for col in Colors().__dir__() if "to" in col]

banner = '''\n\n\n
           ./oyddddddddddhyo:.                                                                     
        -+hdddddddddddddddddddy+.                                                                  
      :yddddddddddddyyssyhddddddds-                                                                
    -yddddddddddds:..---..-/ydddddds.                                                              
   /hddddddddddy-``/sssyy/```:ydddddh-                                                             
  /dddddddddddh.``sh/``.yh-```.sdddddd:                                                            
 :dddddddddddd/ ``sh+..:hhso:``.ddddddh.                                                           
 hdddddddddddd:````/shhs:-:yh+``ydddddds                                                           
:dddddddddddddo`````.hh.```ohs``hddddddd.                                                          
+dddddddddddddd/` ```shy++sho.`/dddddddd:                                                          
+dddddddddddddddo.````:+o+:. `/ddddddddd:                                                          
/dddddddddddddddddo:```````.+hdddddddddd-                                                          
`ddddddddddddddddddddhysyydddddddddddddh                                                           
 +ddddddddddddddddddddddddddddddddddddd:                                                           
 `ydddddddddddddddddddddddddddddddddddo                                                            
  `sdddddddddddddddddddddddddddddddddo`                                                            
   `+ddddddddddddddddddddddddddddddh/                                                              
     -sddddddddddddddddddddddddddho.                                                               
       -ohdddddddddddddddddddddy+.                                                                 
         `:oyhdddddddddddddhy+-`                                                                   
             .-:/+ossso+/:-`
'''
banner1 = '''\n
 ----------------------------------------
  / /____ _____  / /____  ___ ____ ___ /
 /  '_/ // / _ \/ __/ _ \/ _ `/ -_) _ \ /
/_/\_\\_, /\___/\__/\___/\_, /\__/_//_/ /
     /___/              /___/          /
-----------------------------------------
'''


class Col:
    colors = {
            "w": "\033[38;2;255;255;255m",
            "r": "\033[38;2;255;0;0m",
            "g": "\033[38;2;0;255;0m",
            "b": "\033[38;2;0;0;255m"
            }

    white = colors['w']
    red = colors['r']
    green = colors['g']
    blue = colors['b']

    

    def error(*args):
        input(Col.red + '\n' + "".join(args) + Col.white)
        return main()





print(Colorate.Vertical(Colors.blue_to_purple, center(banner, space=60), stop=20))
print(Colorate.Vertical(Colors.blue_to_purple, center(banner1, space=60), stop=20))

amount = int(input('Gen: '))
value = 1,2,3,4,5,6,7,8,9,10,1000

with open("Nitro Codes.txt", "w", encoding='utf-8') as file:
    print("Your nitro codes are being generated, be patient!")

    for i in range(amount):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = 16
        ))

        file.write(f"https://discord.gift/{code}\n")

    print(f"Generated {amount} codes\n")

with open("Nitro Codes.txt") as file:
    for line in file.readlines():
        nitro = line.strip("\n")

        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(f"\n\n Valid | {nitro}\n\n") #If the nitro code will be valid, it will print nitro code leaving two lines for focus xD.
        else:
            print(f"*", end = "")   #It will print "*" if the nitro code won't be valid.

print("\n\n\nYou have generated codes and checked it succesfuly, hope you got some valid ones")
