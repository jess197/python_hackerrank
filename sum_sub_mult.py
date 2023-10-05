'''
Task
The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.
'''

def soma(a,b):
    r = (a+b)
    return r

def sub(a,b):
    r = (a-b)
    return r

def multp(a,b):
    r = (a*b)
    return r


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(soma(a,b))
    print(sub(a,b))
    print(multp(a,b))
    