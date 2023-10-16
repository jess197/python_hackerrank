"""
Given the names and grades for each student in a class of N students,
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically 
and print each name on a new line.

Input Format

The first line contains an integer, , the number of students.
The  subsequent lines describe each student over  lines.
- The first line contains a student's name.
- The second line contains their grade.


Output Format

Print the name(s) of any student(s) having the second lowest grade in. 
If there are multiple students, order their names alphabetically and print each one on a new line.

"""

if __name__ == '__main__':
    grades = []
    grades_scores = []
    students = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        grades.append([name,score])
        grades_scores.append(score)
        
    grades_scores = list(set(grades_scores)) #Getting distinct values for scores
    grades_scores.sort()
    for grade in grades:
        if grade[1] == grades_scores[1]:
            students.append(grade[0])
    
            students.sort()
            
    for student in students:
        print(student)
                        
        
        
        
            
        
        
