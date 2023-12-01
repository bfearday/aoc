# Get calibration values from document

# Part 1

# digits = []
# values = []

# with open("input.txt") as file:
#     for line in file.readlines():
#         digits = [c for i,c in enumerate(line) if c.isdigit()]
#         digit = str(digits[0]) + str(digits[-1])
#         values.append(int(digit))

# values_sum = sum(values)

# print(values_sum)

# Part 2

import re

spelled_digits = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
digits = []
values = []

with open("input.txt") as file:
    for line in file.readlines():
        for key in spelled_digits.keys(): 
            line = re.sub(key, key[0] + spelled_digits[key] + key[len(key)-1], line)
        digits = [c for i,c in enumerate(line) if c.isdigit()]
        digit = str(digits[0]) + str(digits[-1])
        values.append(int(digit))

values_sum = sum(values)
print(values_sum)

