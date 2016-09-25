from random import randint



letters = ("abcdefghijklmnopqrstuvwxyz")

letters_list = []

new = []

for j in range(len(letters)):
  letters_list.append(letters[j])

print(letters_list)

for i in range(len(letters)):
   x = { letters[i] : randint(0,9) }
   new.append(x)

print(new)

output=[]

user_input = input("Enter a letter:")



for char in user_input:
  index = letters_list.index(char)
  num = new[index].get(char)
  output.append(num)


print(output)
