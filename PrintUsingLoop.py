#
nums = [1, 4, 9 ,16, 25, 36, 49, 64, 81, 100]

for i in nums:
    print(i)
    i += 1

x = 36
tup = (1, 4, 9 ,16, 25, 36, 49, 64, 81, 100)

j = 0
while j < len(tup):
    if(tup[j] == x):
        print(tup[j])
    j +=1