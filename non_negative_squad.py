'''
Task
The provided code stub reads and integer, n , from STDIN. For all non-negative integers i < n, print iˆ2.

Example

N = 3

The list of non-negative integers that are less than N = 3  is [0,1,2] . Print the square of each number on a separate line.

0
1
4

'''

def minor(n):
    i = 0
    while(i < n): 
        sqr = i*i
        print(sqr)
        i += 1     

if __name__ == '__main__':
    n = int(input())
    
    minor(n)
