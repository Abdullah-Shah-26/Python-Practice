def product(a = 1,b = 1): # default paramaters will be executed even when we dont pass values
    return a*b
# pehle default parameter nai aa sakta give from last

# can do this to
# def product(a, b=2)
# but not this
# def product(a = 2,b)
print(product())