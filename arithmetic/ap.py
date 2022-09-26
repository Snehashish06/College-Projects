"""      Coded By @CoderX on Telegram!!!        """

#pylint:disable=C0103
#pylint:disable=W0703
#pylint:disable=W0105
#pylint:disable=R0903
from ast import literal_eval as Eve
from time import sleep as sl
from loguru import logger

"""

 •   “S” is the sum of the arithmetic sequence,

 •   “a” as the first term,

 •   “d” the common difference between the terms,

 •   “n” is the total number of terms in the sequence and

 •   “L” is the last term of the sequence.

"""
class AP:
    """To find the sum of n terms"""
    def __init__(self):
        self.a=""
        self.L=""
        self.res=""
        self.__input()

    @classmethod
    def __cleaner(cls):
        print("\033[H\033[2J",end="")

    def __input(self):
        print("\tCoded By Snehashish (CoderX)!!\n\n")
        try:
            self.a=Eve(input("Enter the first term (a): "))
            self.L=Eve(input("Enter the last term (L): "))
        except Exception:
            logger.info("Kindly enter integers only!")
            sl(7)
            self.__cleaner()
            self.__input()
        else:
            self.__sum_of_all()
 
    def __sum_of_all(self):
        s = self.L*(self.L+1)/2
        self.res=s
        return self.res
    
    def __str__(self):
        if ".0" in str(self.res):
            xD=str(self.res).replace(".0","")
            xDD = f"Sum of all numbers between {self.a} and {self.L} is: {xD}"
        else:
            xD=self.res
            xDD= f"Sum of all numbers between {self.a} and {self.L} is: {xD}"
        self.__cleaner()
        return xDD

print(AP())
        
        
        
