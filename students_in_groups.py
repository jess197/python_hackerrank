'''
Please write a program which asks for the number of students on a course and the desired group size. 
The program will then print out the number of groups formed from the students on the course. 
If the division is not even, one of the groups may have fewer members than specified. 

How many students on the course? 8
Desired group size? 4
Number of groups formed: 2

Sample output
How many students on the course? 11
Desired group size? 3
Number of groups formed: 4

'''

# Write your solution here
num_students = int(input("How many students on the course?"))
group_size = int(input("Desired group size? "))

num_groups = num_students // group_size
if num_students % group_size != 0:
    num_groups += 1


print(f"Number of groups formed: {num_groups}")