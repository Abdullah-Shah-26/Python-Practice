# set is the collection of unordered items
# each element in the set must be unique & immutable
# cannot store list and dictionary in sets since they are mutable

collection = {1,2,3,4 ,"hello",2,2,"world"} # duplicates will be ignored

print(collection)
print(len(collection)) # total no of items excluding duplicates

# empty set syntax     if we do collection1 = {} it will become dictionary
collection1 = set()
print(collection1)

