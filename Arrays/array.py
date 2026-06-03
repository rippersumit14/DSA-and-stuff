#for using arrays in python we need to import the array model first in the array
import array

my_array = array.array("i") #in the array function we declare the datatype of the array
print(my_array)
my_array = array.array("i", [3,1,3,2]) #this will declare the array
print(my_array)

#we can also use array in python by using the numpy model
#for that we have to install the numpy model in the terminal

import numpy as np

#*disadvantage of numpy that it is not the part of standard python library we have to install it in the terminal

np_array = np.array([], dtype=int)#this will allocate the memory of zero byte
print(np_array)

np_array1 = np.array([1,2,3,4])#no need to declare the datatype also
print(np_array1)





