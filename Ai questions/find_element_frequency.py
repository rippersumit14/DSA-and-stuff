#in this we have to find the frequency of an element in an array

from array import *

My_array = array("i",[1,2,3,4,2,3,2])

#to find the frequency of the element we will pass the element too as a parameter in the function
def Frequency_find(array1, element):
    count = 0
    for i in array1:
        if element == i:
            count += 1

    return count

print(Frequency_find(My_array, 2))

#the time complexity of this code will be o(n)
#the space complexity of this code will be o(1)

