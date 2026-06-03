#in this we have to delete the element from the array

import numpy as np

arr1 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

#Deletion in 2d numpy array involves creating a new array with updated dimensions and copying the original array
#If we delete row-wise or column-wise in array so the deletion will take place according to that row or column. and create the new 2d array without that row or column

#the time complexity will be o(mn)
#the space complexity will be o(mn) because of the new aray creation with n as the row or column to delete in the new array

newTdarray = np.delete(arr1, 1,axis=0)

print(newTdarray)
