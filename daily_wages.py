'''
Please write a program which asks for the hourly wage, hours worked, and the day of the week.
The program should then print out the daily wages, which equal hourly wage multiplied by hours worked,
except on Sundays when the hourly wage is doubled.
'''

# Write your solution here
hourly_wage = float(input('Hourly wage: '))
hours_worked = int(input('Hours worked: '))
day_week = input('Day of the week: ') 


if day_week == 'Sunday':
    daily_wage = (hourly_wage*2)*hours_worked
else:
    daily_wage = hourly_wage*hours_worked

print(f'Daily wages: {daily_wage} euros')
