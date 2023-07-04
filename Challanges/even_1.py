l = [2, 7, 5, 64, 14, 12, 14, 95, 3]

xD = [i for i in l if i%2==0] # check if even
xD.sort() # accending order
print(*set(xD), sep = ', ') # print unique values
