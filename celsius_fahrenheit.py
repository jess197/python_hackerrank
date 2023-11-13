'''
Please write a program which asks the user for a temperature in degrees Fahrenheit, 
and then prints out the same in degrees Celsius. If the converted temperature falls below zero degrees Celsius,
the program should also print out "Brr! It's cold in here!". 
'''
# Write your solution here
fahrenheit_temp = int(input('Please type in a temperature (F)?'))

celcius_temp = (fahrenheit_temp-32)/1.8


if celcius_temp < 0:
    print(f'{fahrenheit_temp} degrees Fahrenheit equals {celcius_temp} degrees Celsius')
    print("Brr! It's cold in here!")
else:
    print(f'{fahrenheit_temp} degrees Fahrenheit equals {celcius_temp} degrees Celsius')
