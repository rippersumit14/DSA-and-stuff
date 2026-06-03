#in this we have to search for an element in the list

list1 = [1,2,3,4,5,6]

#the first way to search for an element in a list is using in operator
target = 4

if target in list1: #time complexity is o(n) where n is the number of elements in the list
    print(f"the element {target} is there in the list")
else:
    print("Element is not in the list")

#Linear search

target_2 = 3

def linear_search(p_list, p_target):
    for i, value in enumerate(p_list): #enumerate functions iterate over the list while also keeping the track of the index of current item
        if value == p_target:
            return i
    return -1

print(linear_search(list1, target_2))

#the time complexity will be o(n)
#the space complexity will be o(1)



