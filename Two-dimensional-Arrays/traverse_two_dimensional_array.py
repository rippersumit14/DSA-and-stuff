#in this we have to traverse the two-dimensional array

import numpy as np

my_array = np.array([[1,2,3,4], [3,4,5,2], [7,8,9,4]])

print(my_array)

#traversing means visiting all the cells of the array

#when traversing the 2d array we have to finish the first row then the second row. Which means the iteration is done row wise in 2d array

def traverse_array(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])

traverse_array(my_array)

#the time complexity of this code will be o(n^2)
#the space complexity of this code will be o(1)


#*if the number of rows is equal to the column then it will be quadratic time complexity otherwise, it will have o(mn)






