#syantax is <name_of_the_array[index no.]>

from array import *

arr1 = array("i",[1,2,3,4])

def accessElement(array, index):
    if index >= len(array):
        print("There is not element in this index")
    else:
        print(array[index])



#time complexity for this code o(1)
#space complexity for this code o(1)


