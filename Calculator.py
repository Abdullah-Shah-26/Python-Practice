operator = input("Entr your operator:")
n1 = int(input("Enter the first number : "))
n2 = int(input("Enter the second number : "))

if operator == "+":
    print(n1 + n2)
elif operator == "-":
    print(n1 -n2)
elif operator == "*":
    print(n1 * n2)
elif operator == "/":
    print(n1/n2)
elif operator == "//":
    print(n1//n2)
elif operator == "**":
    print(n1**n2)
else:
    print("Invalid operator")