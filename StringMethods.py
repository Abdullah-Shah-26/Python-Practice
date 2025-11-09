print(help(str))

name = input("Enter your full name : ")
phone_no = input("Entr your No : ")

print(len(name))
print(name.find("a")) # first occurrence
print(name.rfind('a')) # last occurrence
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isdigit()) # True or False
print(name.isalpha()) #

print(phone_no.count("-"))
print(phone_no.replace("-",""))