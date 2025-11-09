w = float(input("Enter your weight : "))
unit = input("Kg or Pounds ? (K or L): ")

if unit == 'K':
    w = w * 2.2
    unit = "Lbs"
elif unit == 'L':
    w = w/1.8
    unit = "Kgs"
else :
    print(f"{unit} is invalid.")

print(f"Your weight is  {round(w)} in {unit}")

