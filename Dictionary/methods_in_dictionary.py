#in this first we will look into the pop() method

dict1 = {"1":"sumit","2":"garima","3":"vineet"}
#clear() method does not take any argument
dict1.clear()
print(dict1)

#copy()- shallow copy of dictionary and does not take any parameter
dict2 = {"1":"sumit","2":"garima","3":"vineet"}
dict_copy = dict2.copy()
print(dict_copy)

#fromkeys() method=> creates a new dictionary from given sequence of elements with value provided by user
#it takes two parameter which are (sequence[],value) => 1. sequence of elements, which is used as keys from new dictionary. 2)value is optional, value to be set
dict_fromkeys = dict2.fromkeys([1,2,3], "sumit") #basically modifies the old dict into new dict with different values given by the user
print(dict_fromkeys)


#get()-> gets the key or value which as passed as the parameter in the get() method
get_method = dict2.get("1")
print(get_method)

#items()-> basically it returns the key value pair of the dictionary in the tuples and does not take any parameter
print(dict2.items())

#keys()-> method returns the value of the keys that are present in the dictionary
print(dict2.keys())

#popitem()-> method takes out the arbitrary pair(any random pair) from the dictionary


#setdefault()-> method returns the value of key if key is in the dictionary if not, inserts key with a value to the dictionary.
print(dict2.setdefault("4", "rohal"))
print(dict2)

