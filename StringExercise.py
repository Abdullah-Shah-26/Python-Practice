username = input("Enter a user name: ")

if len(username) >12:
    print("Username too long")
elif not username.find(" ") == -1:
    print("Your username can't contain a spaces")
elif not username.isalpha():
    print("Your username can't contain alphabets")
else :
    print(f"welcome {username}!")

