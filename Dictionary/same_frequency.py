'''
Same Frequency
Define a function which takes two lists as parameters and check if two given lists have the same frequency of elements.

Example:

list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]
check_same_frequency(list1, list2)

Output:
False
'''


def check_same_frequency(list1, list2): # If lengths are different, they can't have same frequency
    if len(list1) != len(list2):
        return False

    # Count frequency of elements in list1
    freq1 = {}
    for item in list1:
        freq1[item] = freq1.get(item, 0) + 1

    # Count frequency of elements in list2
    freq2 = {}
    for item in list2:
        freq2[item] = freq2.get(item, 0) + 1

    # Compare the two frequency dictionaries
    return freq1 == freq2






list1test = [1, 2, 3, 2, 1]
list2test = [3, 1, 2, 1, 3]

print(check_same_frequency(list1test, list2test))
