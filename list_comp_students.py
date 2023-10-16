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

    for _ in range(int(input())):
        name = input()
        score = float(input())

    grades.append([name,score])
    grades_scores.append(score)

    grades_scores = list(set(grades_scores)) 

    grades_scores.sort()

    #This is called a list comprehension (list comp). It's a compact way to create a new list by applying an expression 
    # to each element of an existing list (in this case, the grades list) while also applying a condition.
    students = [grade[0] for grade in grades if grade[1] == grades_scores[1]]
    students.sort()

    """
    So, the list comprehension is essentially creating a new list (students)
    that contains the names of students (grade[0]) whose score is equal to the second-lowest score (grades_scores[1]). 
    It does this by iterating through the grades list and applying the condition.
    
    """
    
    print(*students, sep = "\n") 

    """
    The asterisk (*) is used for unpacking a list or iterable. In this context, it takes each element (student name) 
    in the students list and passes them as separate arguments to the print function. This means that each student 
    name will be printed one after the other without any enclosing brackets or commas.

    sep="\n": The sep parameter in the print function specifies the separator that should be used between the items 
    being printed. In this case, it is set to "\n", which represents a newline character. This means that
    each item (student name) will be separated by a newline, causing each name to be printed on a new line.
    """


