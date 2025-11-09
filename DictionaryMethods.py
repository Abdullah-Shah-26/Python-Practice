
student = {
    "name" : "DIYA SARDA",
    "subject" : {
        "maths" : 100,
        "english" : 99,
    }
}

# to get all keys of dictionary
print(student.keys())
# this can be type cast to normal list or tuple
print(list(student.keys()))
# to get total keys of dictionary
print(len(list(student.keys())))
# to get values
print((student.values()))

# .items() - returns the key val pairs of dictionary as tuple
print(student.items())

pairs = list(student.items())
print(pairs[0])

# .get("key") returns the key acc to value
print(student.get("name")) # but this will return None
print(student["name"]) # is if mistakenly write a key that doesnt exist it will give error


# inserts a specified items in dictionary

new_dict = {"school" : "LFHS" , "city" : "HYD", }
student.update(new_dict)
print(student)
