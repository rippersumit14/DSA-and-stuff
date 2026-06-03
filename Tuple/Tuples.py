#tuples are the immutable sequence of python objects

my_tuple = ('a','b','c','d','f')
print(my_tuple)

new_tuple = tuple(my_tuple)

print(new_tuple)

#the time complexity of creating a tuple is o(1)
#hthe space complexity of creating a tuple is o(n)

#how to access the elements of tuple
#bracket operator is used to access the element of the tuple
print(my_tuple[2]) #index of the tuple


#we can also access the tuple using the slice operator [:]
#[left_index:right_index]
print(my_tuple[1:4])




