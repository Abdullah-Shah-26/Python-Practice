# bro of lists
# tuple lets us create immutable sequences of values like strings

tup = (1, 2, 3, 4)
print(tup)
print(type(tup))
print(tup[0])

# tup[0] = 5 # not allowed in tuple

tup1 = () # empty tuple
print(tup1)

tup2 = (1,) # correct way to write single value tuple
tup3 = (1) # python thinks that its an int surrounded by paranthesis
print(tup2)
print(tup3)

tup4 = ("hello",)
print(tup4)
