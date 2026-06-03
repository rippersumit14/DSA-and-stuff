#in this we have to find the missing number of array size n - 1 contains number 1 to N
#input: 5
#1 2 3 5

#output = 4

from array import *

# Input: The array and the value of N
arr1 = array("i", [1, 2, 3, 5])
N = len(arr1) + 1


def find_missing_number(array1, n):
    # 1. Calculate what the sum SHOULD be (1 to N)
    # Formula: (n * (n + 1)) / 2
    expected_sum = n * (n + 1) // 2

    # 2. Calculate the ACTUAL sum of the elements we have
    actual_sum = sum(array1)

    # 3. The difference is the missing number
    return expected_sum - actual_sum


# Output the result
result = find_missing_number(arr1, N)
print(f"The missing number is: {result}")

#The time complexity of this code will be o(n)
#The space complexity of this code will be o(1)


