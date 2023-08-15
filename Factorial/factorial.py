from typing import Optional


class Factorial:


    def __init__(self):
        print(f"\033[1m\033[101m\033[35mCoded by Snehashish (CoderX)\033[0m:") #!   Credits

    def with_logical_work(self, number: Optional[int] = 0) : # Takes only one parameter and is optional
        if number < 0:raise ValueError(f'Can\'t use negative {number = }') # if negative raise ValueError
        factorial_ = 1
        for i in range(1, number+1):factorial_ *= i # increment factorial_ variable to get the end result
        return factorial_ # return Value
    
    def without_logical_work(self, num: Optional[int] = 0):
        ''' well you didn't specify to write whole logic or to write from scratch tho I am writing both with and without logic'''
        return __import__('math').factorial(num)

    def call_both(self, num: int):
        return f"{self.with_logical_work(num)}\n{self.without_logical_work(num)}"

    def siso(*args, **kwargs):
        __import__('sys').stdout.write(*args, *kwargs)


if __name__ == "__main__":
    Factorial.siso(Factorial().call_both(3)) # call class instance and print the value
