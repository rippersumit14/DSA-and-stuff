from array import *

arr1 = array("i",[1,2,4,5])
N = len(arr1) + 1

def missing_number_in_array(array1, n):
    array1_sum = sum(array1)
    missing_number_sum = 0
    for i in range(n + 1):
        missing_number_sum = missing_number_sum + i

    return  missing_number_sum - array1_sum

print(missing_number_in_array(arr1, N))

#the time complexity of this code will be o(n)
#the space complexity of this code will be o(1)



