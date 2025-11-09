n = int(input("enter a no to get sum : "))
i = 1
sum = 0
while i <= n:
    sum += i
    i += 1

print(sum)

for i in range(1 , n+1):
    sum += i
    i += 1


N = int(input("enter a no to get its factorial : "))
# print factorial of first n numbers
fact = 1
for i in range(1, N + 1):
    fact *= i

print(fact)


