list = [13, 2, 3]

list.append(4) # adds one element at end # returns None
print(list)
            # sorting in ascending order
list.sort() # changes the original string
print(list)

# sort in descending order
list1 = ["mango","banana","apple"]
print(list1.sort(reverse = True))
print(list1.sort())
print(list1)

# reverse original string
list1.reverse()
print(list)
#insert element at index
list.insert(2,"INDIA")
print(list)
#remove first occurence of element
list.remove("INDIA")
print(list)
# remove index at particular idex
list.pop(2)
print(list)