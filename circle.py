import math

r = float(input("enter the radius : "))
print(f"The circumferance of circle is : {round(2 * math.pi * r)} cm")
area = math.pi * (r ** 2)
print(f"The area of circle is : {round(area)} cm^2")