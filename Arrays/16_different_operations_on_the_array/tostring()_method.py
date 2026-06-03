#in this we convert the array into string using toString() method
import array

arr1 = array.array("i", [1, 2, 3, 4, 5])

byte_data = arr1.tobytes()#in modern python we use tobytes()
print(byte_data)

