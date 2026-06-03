#in this we will access the element of 2d array

import numpy as np

my_array = np.array([[1,2,3],[23,2,3],[22,1,3]])

#In two-dimensional array we have two indexes which are [row][column]

def access_element(array, rowIndex, colIndex):
    if rowIndex >= len(array) and colIndex >= len(array[0]): #this will return the row if we just use the len() and for column len(array[0])
        print("Incorrect index")
    else:
        print(array[rowIndex][colIndex]) #[rows][columns]

access_element(my_array, 1, 1)

#the time complexity of this code will be o(n)
#the space complexity of this code will be o(1)






