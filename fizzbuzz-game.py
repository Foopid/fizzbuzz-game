# FizzBuzz Game
# Author: Foopid
# Description:
# Prints numbers from 1 to N (set by 'count').
# - Multiples of 3 → "Fizz"
# - Multiples of 5 → "Buzz"
# - Multiples of both → "FizzBuzz"

count = 100  # Change this to adjust the range

for i in range(1, count + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
