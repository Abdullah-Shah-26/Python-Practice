def fact(n):
    factorial = 1
    for i in range(1,n+1):
        factorial *= i
    return factorial

def calfact(n):
    fact = 1
    i = 1
    while i <= n:
        fact *= i
        i += 1
    print(fact)

print(fact(10))
calfact(10)