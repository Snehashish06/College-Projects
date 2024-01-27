import re
import os

from time import sleep
from datetime import datetime

from . import LOGGER
from .clear_screen import clear
from .Animation.animation import l_l
from .database.if_initial import h_h
from .Color.color_class import color
from .database.main_db import update, get
from .CoderX.CoderX import xD1, xDD


def initial_work(CoderX: bool = False):
    if CoderX!=True:
        exit("\033[31;1mAccess denied!\033[0m")
    clear()
    os.system("title Hui HUi It was coded by Snehashish (CoderX)")
    os.system("color 3")
initial_work(1)

name = input("What is your name?: ")
class Main:

    def __init__(self):
        what_to = 3
        tdt = datetime.now().__str__().split()
        d = tdt[0].split('-')
        formatted_date = f"{d[-1]}-{d[-2]}-{d[-3]}"
        formatted_time = re.sub("\.......$", "", tdt[1])
        clear()
        print(xD1, xDD)
        print(f"\n\033[35m\033[1mHello {name}! How are you?\n\033[32m  ]> Date today: {formatted_date}\n  \033[21m ]> Current time: {formatted_time}\033[0m")
        try:
            what_to = int(input(f"\n\033[1;4mᴄʜᴏᴏꜱᴇ ᴀɴ ᴏᴘᴛɪᴏɴ\033[0m:\n\t{color.color(color.BLACK, '[0]: Exit')}\n\t{color.color(color.RED, '[1]: Add new borrower')}\n\t{color.color(color.GREEN, '[2]: Delete borrower')}\n\t{color.color(color.BLUE, '[3]: Get all borrowers')}\n\n\033[1;96m ]> 𝐘𝐨𝐮𝐫 𝐒𝐞𝐥𝐞𝐜𝐭𝐢𝐨𝐧 : \033[0m"))
        except ValueError:
            LOGGER.error("Kindly enter a valid number.")
            sleep(2)
            clear()
            Main()
        if what_to == 0:
            exit()
        elif what_to == 1:
            self.__new_borrower_()
        elif what_to == 2:
            self.__del_borrower_()
        elif what_to == 3:
            self.__get_all_borrowers()
    

    def __input(self):
        input("\nPress enter to continue")

    def __new_borrower_(self):
        name = input("\n\nWhat's the name of the borrower?: ")
        amount = int(input("How much did they borrow?: "))
        update.new_borrower(name, amount)
        print("Updated database...")
        self.__input()
    
    def __del_borrower_(self):
        name = input("\n\nWhat's the name of the borrower?: ")
        amount = input("How much did they return?: ")
        update.del_borrower(name, amount)
        print("Updated database...")
        self.__input()
    
    def __get_all_borrowers(self):
        print("\n")
        print(get.get_borrowers())
        self.__input()

while True:
        Main()
