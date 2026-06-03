#in this we will search for an element in a dictionary

dict1 = {"1":"sumit","2":"garima","3":"vineet"}

def Search_elements(dict, element): #linear search
    for key in dict:
        if dict[key] == element:
            return key, element


    return "The value does not exist"

print(Search_elements(dict1, "vineet"))

#the time complexity of this code will be o(n)
#the space complexity of this code will be o(1)



