#in this we have been given an array and a number D, rotate the array to the left by D positions
#input : 5
#1 2 3 4 5
#2

#ouput: 3 4 5 1 2

from array import *

arr1 = array("i", [1, 2, 3, 4, 5])

D = int(input("Enter D: "))


def Rotate_array_elements(array1, D):
    n = len(array1)

    # handle case when D > length
    D = D % n

    for _ in range(D): #_ use but don't care about
        temp = array1[0]  # store first element

        for i in range(n - 1):  # shift elements left
            array1[i] = array1[i + 1]

        array1[n - 1] = temp  # put first element at end


Rotate_array_elements(arr1, D)
print(arr1)


