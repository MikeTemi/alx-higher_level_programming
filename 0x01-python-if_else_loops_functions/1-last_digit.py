#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10
if number < 0:
    digit = -digit
print(f"Last digit of {number} is {digit} and is", end=" ")
if digit > 5:
    print(f"greater than 5", end="\n")
elif digit == 0:
    print(f"0", end="\n")
else:
    print(f"less than 6 and not 0", end="\n")