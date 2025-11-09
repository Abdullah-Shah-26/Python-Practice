marks = [29, 99.9, 81, 88, 100]
print(marks)
print(type(marks))
print(marks[0])
print(len(marks))
# lists can store different types of data together unlike array/vectors
student = [100,"karan",'delhi']
print(student)

# list are mutable(changeable) in python
# string are immutable
str = "hello"
print(str[1])
str[0] = 'H' # This is invalid
print(str)

student[0] = "arjun"
print(student)
