# dictionary - needs curly braces
# it is mutable - they are unordered - no duplicate keys allowed
info = {
    "key" : "value",
    "name" : "JOhn",
    "age" : 18,
    "marks" : [99, 98 , 98 , 90], # list
    "subject" : ("C++", "Java"), # tuple
    10 : 99,
}
print(type(info))


info["name"] = "panda" # to change values
print(info["name"]) #dict["name"] // to access values
print(info["age"])

# to add new key value pair to dictionary
info["surname"] = "shah"
print(info)

# can create null dictionary too
null_dict = {}
null_dict["name"] = "diya"
print(null_dict)
