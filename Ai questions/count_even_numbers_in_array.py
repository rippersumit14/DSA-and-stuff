#in this we have to count the even numbers in the array

from array import *

arr1 = array("i", [1,2,3,4])

def Even_count(array_1):
    count = 0
    for i in array_1:
        if i % 2 == 0:
            count += 1

    return  count

print(Even_count(arr1))



#the time complexity of this code will be o(n)
#the space complexity of this code will be o(1)

