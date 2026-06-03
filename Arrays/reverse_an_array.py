#in this we have to reverse an array without using an extra array
#so in this question the space complexity will be o(1)

from array import *
arr1 = array("i", [1,2,3,4,5])

def reverse_array(reversed_array):
    start = 0
    end  = len(reversed_array) - 1


    while start < end:
        reversed_array[start], reversed_array[end] = reversed_array[end], reversed_array[start]


        start += 1
        end -= 1

reverse_array(arr1)
print(arr1)

#the space complexity will be o(1)
#the time complexity will be o(n)







