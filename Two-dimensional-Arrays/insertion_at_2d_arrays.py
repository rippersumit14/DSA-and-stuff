#in this we have to perform insertion in 2-d array

#there are two different ways of adding elements in 2-d array
#1)Addition of columns 2)Addition of rows

#1)shifting of elements via columns
#the time complexity will be o(mn)

#2)each row will move 1 step down. Shifting of the rows will be there
#the time complexity will be o(mn)

import numpy as np

My_array = np.array([ #3x4 matrix
    [11,22,33,44],
    [5,6,7,8],
    [9,10,11,12]
])

new_array = np.insert(My_array, 0, [1,2,3], axis=1)#if axis is said to 1 then it will add the column wise and if it is said to 0 then it will add row wise
print(new_array)

#we could also use the append method here to add the elements in the last
new_array1 = np.append(My_array, [[1,2,3,4]], axis=0)
print(new_array1)

#the time complexity will be o(mn)






