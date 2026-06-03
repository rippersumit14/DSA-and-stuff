#Get array buffer information through buffer_info() method
import array
arr1 = array.array("i", [1,2,3,4,5])
print(arr1.buffer_info())

#this method tells that where our array is stored in the memory and how much space does it take to store
