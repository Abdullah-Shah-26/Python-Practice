def factorial(n):
    if n == 1 or n == 0 :
        return 1

    return n * factorial(n-1)

n = factorial(5)
print("The factorial of given no is : " ,n)