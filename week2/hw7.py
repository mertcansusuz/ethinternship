from random import randint

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


new = []
output=[]

for i in range(len(letters)):
   x = { letters[i] : randint(0,9) }
   new.append(x)
print(new)

user_input = input("Enter a letter:")

for char in user_input:
  index = letters.index(char)
  num = new[index].get(char)
  output.append(num)


print(output)
