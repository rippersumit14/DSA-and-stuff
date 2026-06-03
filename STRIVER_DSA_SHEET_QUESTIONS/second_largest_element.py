def find_second_elements(nums):
    n = len(nums)

    if n < 2:
        return -1, -1   # Not possible

    smallest = float('inf')
    second_smallest = float('inf')

    largest = float('-inf')
    second_largest = float('-inf')

    for num in nums:

        # For smallest and second smallest
        if num < smallest:
            second_smallest = smallest
            smallest = num

        elif smallest < num < second_smallest:
            second_smallest = num

        # For largest and second largest
        if num > largest:
            second_largest = largest
            largest = num

        elif second_largest < num < largest:
            second_largest = num

    # Handle edge cases
    if second_smallest == float('inf'):
        second_smallest = -1

    if second_largest == float('-inf'):
        second_largest = -1

    return second_smallest, second_largest

#the time complexity will be o(n)
#the space complexity will be o(1)


#Testing some stuff
print(2 % 4)
print(2 / 4)
print(2 // 4)