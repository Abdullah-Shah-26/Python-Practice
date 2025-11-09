str = "i am genius"
print(str.endswith("ius")) # returns true or false

print(str.capitalize()) # capitalize the first char of string doesn't make changes to original string

str1 = str.replace("i","a") # replaces all occurrence of old value , doesn't change in original string
str2 = str.replace("genius","prodigy")
print(str2)

print(str.find("a")) #searches a word in a string and returns the idx of its first occurrence

print(str.count("am")) # how many times did this word occur in string