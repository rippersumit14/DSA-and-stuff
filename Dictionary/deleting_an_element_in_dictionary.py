#in this we will look in deleting the element in a dictionary
#various ways
#del statement

dict1 = {"1":"sumit","2":"garima","3":"vineet"}

del dict1['3']#delets the element by identifying the actual key
print(dict1)
#the time complexity of del is o(1)
#the space complexity of del is also o(1)

#2nd method pop() method

dict1.pop('1') #the time complexity of this code will be o(1)
print(dict1)#space also o(1)

#clear() to clear the dictionary

