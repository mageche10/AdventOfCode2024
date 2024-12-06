import re

suma = 0
with open('input3.txt') as file:
    text = file.read()

    matches = re.findall(r'mul\(\d*,\d*\)', text)

    for match in matches:
        numbers = match[4:-1].split(',')
        suma = suma + int(numbers[0]) * int(numbers[1])

print(suma)

# PART 2

suma = 0
with open('input3.txt') as file:
    text = file.read()

    matchesDo = re.split(r"do\(\)", text)
    goodString = ""
    for match in matchesDo:
        goodString = goodString + re.split(r"don\'t\(\)", match)[0]

    matches = re.findall(r'mul\(\d*,\d*\)', goodString)

    for match in matches:
        numbers = match[4:-1].split(',')
        suma = suma + int(numbers[0]) * int(numbers[1])

print(suma)