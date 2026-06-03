#in this we will insert and update the elements of a list

list1 = [1,1,2,4,3]

list1.insert(1,6) #insert method takes the 2 parameters which are index and object which will be the element need to be inserted
print(list1)

list1.append(4)
print(list1)# using the append method we can add the elements in the last of the list

list2 = [1,2,4,5]
list1.extend(list2)#extends method extends the list with the new list which will passed as the parameter in the args
print(list1) #the space complexity of this extend operation will be o(n).

