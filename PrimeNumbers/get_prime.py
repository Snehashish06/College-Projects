# Compressed Code
def chk_prime(num): # get parameter
    for i in range(2, num): #loop
        if num % i == 0:break  # check if not prime
    else:return num # return prime

for i in range(1, 100): #loop
    if chk_prime(i) != None:print(f"\033[31m\033[1m{chk_prime(i)}\033[0m") # call funtion and print result
