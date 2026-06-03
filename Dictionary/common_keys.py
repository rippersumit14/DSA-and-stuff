'''
Common Keys
Define a function with takes two dictionaries as parameters and merge them and sum the values of common keys.

Example:

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
merge_dicts(dict1, dict2)
Output:

{'a': 1, 'b': 5, 'c': 7, 'd': 5}'''

def merge_dicts(dict1, dict2):
    merge_dictionaries = {}
    merge_dictionaries.update(dict1) #we could also use the copy() method for that

    for key, value in dict2.items():
        if key in merge_dictionaries:
            merge_dictionaries[key] += value
        else:
            merge_dictionaries[key] = value

    return merge_dictionaries


dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

print(merge_dicts(dict1, dict2))


#the time complexity of this code will be o(n)
#the space complexity of this code will be o(n)



