# set is mutable - we can insert / delete / modify
# but set - elements are immutable that why we cant pass list and dictionary

collection = set()
collection.add(1)
collection.add(2)
collection.add("hello")
collection.add((1,2,3,4)) # tuple
# collection.add([1,2,3]) # cant pass list
collection.remove(2)



print(collection.pop())# removes a random value
# collection.clear() # clears the whole set


print(collection)

#union of sets # combines the values of both sets like in math
set1 = {1,3,4,5}
set2 = {1, 10, 20 ,30}

print(set1.union(set2)) # it returns the new set doesn't make changes to old set
print(set1.intersection(set2)) # returns the common value of both set in a new set
