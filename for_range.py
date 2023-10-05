'''
The included code stub will read an integer, , from STDIN.

Without using any string methods, try to print the following:


Note that "" represents the consecutive values in between.

Example

Print the string .

Input Format

The first line contains an integer .

Constraints


Output Format

Print the list of integers from  through  as a string, without spaces.
'''

def rng(n):
    lst = '1'
    for num in range(2,n+1):
        lst = lst+str(num)
    return lst
 


if __name__ == '__main__':
    n = int(input())
    print(rng(n))
