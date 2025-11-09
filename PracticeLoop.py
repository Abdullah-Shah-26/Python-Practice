list = [1, 4, 9, 16, 25, 36, 49]

for i in list:
    print(i)

j = 0
while j < len(list):
    print(list[j])
    j+=1

# search a no x in tuple
tup = (1, 4, 9, 16, 25, 36, 49)
x = 49
idx = 0
for n in tup:
        if n == x :
            print("Element found at index : ", idx)
        idx += 1