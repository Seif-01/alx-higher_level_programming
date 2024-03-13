#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10

if number < 0:
    last_digit = -last_digit

print("Last digit of", number, "is", last_digit, end=" ")

if int(last_digit) == 0:
    print("is 0")
elif int(last_digit) > 5:
    print("and is greater than 5")
else:
    print("and is less than 6 and not 0")