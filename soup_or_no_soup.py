""" 
Please write a program which asks for the user's name. If the name is anything but "Jerry", 
the program then asks for the number of portions and prints out the total cost.
The price of a single portion is 5.90.
"""

# Write your solution here
name = input("Please tell me your name: ")

if name != "Jerry":
    portions = int(input("How many portions of soup? "))
    total_cost = portions*5.90
    print(f"The total cost is {total_cost}")
print("Next please!")