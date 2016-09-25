#took it from stackoverflow

import random
input = raw_input('Write Text: ')

output = []

for character in input:
    number = ord(character) - 96
    output.append(number)
print output
