a = int(input("Enter a no : "))
b = int(input("Enter b no : "))
c = int(input("Enter c no : "))

if(a > b ):
    if(a > c):
        print("a is greatest")
    else:
        print("c is greatest")
elif(b > a ):
    if(b > c):
        print("b is greatest")
    else:
        print("c is greatest")
else:
    print("c is greatest")

