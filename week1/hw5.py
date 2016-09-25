from random import randint



letters = ("abcdefghijklmnopqrstuvwxyz")

new = []

for i in range(len(letters)):
   x = { letters[i] : randint(0,9) }
   new.append(x)

print new


output = []
input = raw_input("letter: ")
for char in input:
    num = new[i].get("char")
    output.append(num)
print output
