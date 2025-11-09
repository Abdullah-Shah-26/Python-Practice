set1 = {"python","java","C++","python","javascript"}
set2 = {"java","python","java","C++","C"}

print("Total no of classroom required : ",len(set1.union(set2)))

# or we can use only one set

subjects = {
"python","java","C++","python","javascript","java","python","java","C++","C"
}
print(len(subjects))