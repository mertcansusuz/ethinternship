import random

letters = ("abcdefghijklmnopqrstuvwxyz")
numbers = [1,2,3,4,5,6,7,8,9,0]
new = []
for i in letters:
    x = ord(i) - 96
    new.append(x)


print new


