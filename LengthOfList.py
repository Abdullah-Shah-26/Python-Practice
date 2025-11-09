def list_len(list):
    return (len(list))

def list_elem_in_singleline(list):
    for item in list:
        print(item , end =" ")

my_list = [1,2,3,4,5]
print(list_len(my_list))
list_elem_in_singleline(my_list)