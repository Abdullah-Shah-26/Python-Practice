marks = int(input("Enter your marks: "))

if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
else:
    grade = "C"

print(grade)