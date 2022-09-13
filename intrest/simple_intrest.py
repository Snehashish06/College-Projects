"""Simple intrest finder by @CoderX on telegram"""

import sys
import datetime
from time import sleep as sl
from os import system as sy
from ast import literal_eval as Eve

class SimpleIntrest:

    def __init__(self):
        self.__input()
        self.Principal=""
        self.Time=""
        self.Rate=""
        self.m_d_y=""
        self.answer="Unable to calculate"

    def __str__(self):
        return self.answer

    def __input(self):
        try:
            self.Principal = Eve(input("Enter the principal ammount: "))
            self.Time = Eve(input("Enter month or day or year: "))
            self.Rate = Eve(input("Enter rate of interest: "))
            sy("clear")
        except Exception:
            print("Kindly enter a valid Integer don't use your brain much!")
            sl(5)
            sy("clear")
            self.__input()
        else:
            self.__Time()
            
    def __Time(self):
        self.m_d_y = input("""What did you enter?
year or month or day?: 
        M = Month(s)
        Y = Year(s)
        D = Day(s)

Enter a valid input!!: """).lower()
        sy("clear")
        self.__input_checker()
    
    def __input_checker(self):
        i=self.m_d_y
        if i!="y" and i!="m" and i!="d":
            self.answer="Wrong input {}!".format(i)
            sl(5)
            self.__Time()
        else:
            self.__main__()

    def __main__(self):
        print("Im running now\nMain func is now.running\n\n")
        i=self.m_d_y
        p=self.Principal
        n=self.Time
        r=self.Rate

        if i=="m":
            _D=f"₹{p*n*r/100:,}"
            if ".0" in _D:
                a_n_s=_D.replace(".0", "")
            else:
                a_n_s=_D
            self.answer=a_n_s
            print(f"This print is from main function {a_n_s}\n\nActual answer:")

print(SimpleIntrest())
            
