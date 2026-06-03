#in this we have to print the sum of array

from array import *

arr1 = array("i",[1,2,3,4])

def sum_array(array_sum):
    sum = 0
    for i in array_sum:
        sum += i
    return sum

print(sum_array(arr1))


#the time complexity of this code will be o(n)
#the space complexity of this code will be o(1)
