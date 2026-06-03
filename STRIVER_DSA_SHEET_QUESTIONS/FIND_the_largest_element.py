'''Problem Statement: Given an array, we have to find the largest element in the array.

Examples
Example 1:
Input:
 arr[] = {2, 5, 1, 3, 0}
Output:
 5
Explanation:

5 is the largest element in the array.

Example 2:
Input:
 arr[] = {8, 10, 5, 7, 9}
Output:
 10
Explanation:

10 is the largest element in the array.'''

arr = [1,2,3,4,5]

maxy = arr[0]

for i in arr:
    if i > maxy:
        maxy = i
    else:
        maxy = maxy

second_maxy = arr[maxy-1]
print(second_maxy)