#!/usr/bin/python3
import random

# Generate a random signed number between -10 and 10 (inclusive)
number = random.randint(-10, 10)

# Check the value of the number and print the appropriate message
if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is negative")

