"""
Please write a program which asks the user for an integer number. If the number is less than zero,
the program should print out the number multiplied by -1. Otherwise the program prints out the number as is.
"""

# Write your solution here
number = int(input("Please type in a number: "))

if number < 0: 
    number = number*-1
    print(f"The The absolute value of this number is {number}")
else:
    print(f"The The absolute value of this number is {number}")