str = "HOW ARE YOU ?"
for i in str:
    if(i == 'E'):
        print("E found : ")
        break
    print(i)
else:# when we use break and if we dont use optional else last statment will be executed
    print("END")