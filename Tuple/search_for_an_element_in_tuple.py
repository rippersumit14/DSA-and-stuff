#in this we will search for any element in the tuple




my_tuple = ('a','b','c','d')

#in operator
if 'a' in my_tuple:
    print("True")

print(my_tuple.index('c'))


#performing linear search in a tuple
def search_element(tuple_name, element):   #time complexity of o(n)
    for i in range(len(tuple_name)):
        if tuple_name[i] == element:
            return f"The {element} is found at the {i} index"
    return "Not found"

print(search_element(my_tuple, 'd'))



