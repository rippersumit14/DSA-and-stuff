'''
Key with the Highest Value
Define a function which takes a dictionary as a parameter and returns the key with the highest value in a dictionary.

Example:

my_dict = {'a': 5, 'b': 9, 'c': 2}
max_value_key(my_dict))
Output:
b

'''

my_dict = {'a': 5, 'b': 9, 'c': 2}

def max_value_key(dictionary):
    # get the first key-value pair
    current_key, current_maximum_value = next(iter(dictionary.items()))

    # loop through remaining items
    for key, value in dictionary.items():
        if value > current_maximum_value:
            current_maximum_value = value
            current_key = key

    return current_key

print(max_value_key(my_dict))






