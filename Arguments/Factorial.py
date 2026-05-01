# find the factorial of the given number

n = int(input("Enter any number to find its factorial : "))

def factorial(n):

    if n==0 or n==1:

        return 1

    else:

        return n * factorial(n-1)

print(factorial(n))