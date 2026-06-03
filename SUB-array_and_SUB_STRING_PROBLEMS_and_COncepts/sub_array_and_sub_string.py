"""
SUBARRAY, SUBSTRING, SLIDING WINDOW, PREFIX SUM, SUFFIX SUM

This file is for practice + revision.

Important:
- Subarray = continuous part of an array/list
- Substring = continuous part of a string
- Sliding Window = technique to move through continuous parts efficiently
- Prefix Sum = sum from start to current index
- Suffix/Postfix Sum = sum from current index to end
"""


# --------------------------------------------------
# 1. SUBARRAY BASICS
# --------------------------------------------------

def print_all_subarrays(arr):
    """
    Subarray means continuous part of an array.

    Example:
    arr = [1, 2, 3]

    Subarrays:
    [1], [1, 2], [1, 2, 3]
    [2], [2, 3]
    [3]

    Time Complexity: O(n^2)
    """
    n = len(arr)

    for start in range(n):
        for end in range(start, n):
            print(arr[start:end + 1])


# --------------------------------------------------
# 2. SUBSTRING BASICS
# --------------------------------------------------

def print_all_substrings(s):
    """
    Substring means continuous part of a string.

    Example:
    s = "abc"

    Substrings:
    "a", "ab", "abc"
    "b", "bc"
    "c"
    """
    n = len(s)

    for start in range(n):
        for end in range(start, n):
            print(s[start:end + 1])


# --------------------------------------------------
# 3. FIXED SIZE SLIDING WINDOW
# --------------------------------------------------

def max_sum_subarray_size_k(arr, k):
    """
    Problem:
    Find maximum sum of subarray of size k.

    Example:
    arr = [2, 1, 5, 1, 3, 2]
    k = 3

    Windows:
    [2,1,5] = 8
    [1,5,1] = 7
    [5,1,3] = 9
    [1,3,2] = 6

    Answer = 9

    Sliding Window:
    - Add new element from right
    - Remove old element from left

    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    if k > len(arr):
        return None

    window_sum = sum(arr[:k])
    max_sum = window_sum

    for right in range(k, len(arr)):
        window_sum += arr[right]        # add new element
        window_sum -= arr[right - k]    # remove old left element

        max_sum = max(max_sum, window_sum)

    return max_sum


# --------------------------------------------------
# 4. VARIABLE SIZE SLIDING WINDOW
# --------------------------------------------------

def longest_subarray_sum_less_equal_k(arr, k):
    """
    Problem:
    Find length of longest subarray whose sum <= k.

    Example:
    arr = [2, 1, 5, 1, 3, 2]
    k = 6

    Valid subarrays:
    [2,1] sum = 3
    [1,5] sum = 6
    [5,1] sum = 6
    [1,3,2] sum = 6

    Answer = 3

    Variable Sliding Window:
    - Expand right pointer
    - If condition breaks, move left pointer

    Works best when array has positive numbers.
    """

    left = 0
    current_sum = 0
    max_length = 0

    for right in range(len(arr)):
        current_sum += arr[right]

        while current_sum > k:
            current_sum -= arr[left]
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length


# --------------------------------------------------
# 5. PREFIX SUM
# --------------------------------------------------

def build_prefix_sum(arr):
    """ r fd c
    Prefix Sum:
    prefix[i] stores sum from index 0 to i.

    Example:
    arr = [1, 2, 3, 4]

    prefix = [1, 3, 6, 10]

    Meaning:
    prefix[0] = 1
    prefix[1] = 1 + 2 = 3
    prefix[2] = 1 + 2 + 3 = 6
    prefix[3] = 1 + 2 + 3 + 4 = 10
    """

    prefix = [0] * len(arr)

    prefix[0] = arr[0]

    for i in range(1, len(arr)):
        prefix[i] = prefix[i - 1] + arr[i]

    return prefix


def range_sum(prefix, left, right):
    """
    Find sum from index left to right using prefix sum.

    Formula:
    sum(left to right) = prefix[right] - prefix[left - 1]

    If left == 0:
    sum = prefix[right]
    """

    if left == 0:
        return prefix[right]

    return prefix[right] - prefix[left - 1]


# --------------------------------------------------
# 6. SUFFIX / POSTFIX SUM
# --------------------------------------------------

def build_suffix_sum(arr):
    """
    Suffix/Postfix Sum:
    suffix[i] stores sum from index i to last index.

    Example:
    arr = [1, 2, 3, 4]

    suffix = [10, 9, 7, 4]

    Meaning:
    suffix[0] = 1 + 2 + 3 + 4 = 10
    suffix[1] = 2 + 3 + 4 = 9
    suffix[2] = 3 + 4 = 7
    suffix[3] = 4
    """

    n = len(arr)
    suffix = [0] * n

    suffix[n - 1] = arr[n - 1]

    for i in range(n - 2, -1, -1):
        suffix[i] = arr[i] + suffix[i + 1]

    return suffix


# --------------------------------------------------
# 7. PREFIX SUM + HASHMAP
# --------------------------------------------------

def subarray_sum_equals_k(arr, k):
    """
    Problem:
    Count subarrays whose sum equals k.

    Example:
    arr = [1, 2, 3]
    k = 3

    Valid subarrays:
    [1,2]
    [3]

    Answer = 2

    Logic:
    current_sum = sum from start to current index

    If:
    current_sum - k existed before

    Then:
    there is a subarray ending here with sum k.

    This is very important for interviews.
    """

    prefix_count = {0: 1}
    current_sum = 0
    count = 0

    for num in arr:
        current_sum += num

        needed_sum = current_sum - k

        if needed_sum in prefix_count:
            count += prefix_count[needed_sum]

        prefix_count[current_sum] = prefix_count.get(current_sum, 0) + 1

    return count


# --------------------------------------------------
# 8. SUBSTRING SLIDING WINDOW
# --------------------------------------------------

def longest_substring_without_repeating(s):
    """
    Problem:
    Find length of longest substring without repeating characters.

    Example:
    s = "abcabcbb"

    Answer = 3

    Longest substring:
    "abc"

    Logic:
    - Use left and right pointers
    - Use set to track characters inside current window
    - If duplicate comes, move left pointer
    """

    left = 0
    seen = set()
    max_length = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length


# --------------------------------------------------
# 9. PRACTICE RUN
# --------------------------------------------------

if __name__ == "__main__":
    arr = [2, 1, 5, 1, 3, 2]
    s = "abcabcbb"

    print("All subarrays:")
    print_all_subarrays([1, 2, 3])

    print("\nAll substrings:")
    print_all_substrings("abc")

    print("\nMax sum subarray of size k:")
    print(max_sum_subarray_size_k(arr, 3))

    print("\nLongest subarray with sum <= k:")
    print(longest_subarray_sum_less_equal_k(arr, 6))

    print("\nPrefix sum:")
    prefix = build_prefix_sum([1, 2, 3, 4])
    print(prefix)

    print("\nRange sum from index 1 to 3:")
    print(range_sum(prefix, 1, 3))

    print("\nSuffix/Postfix sum:")
    print(build_suffix_sum([1, 2, 3, 4]))

    print("\nCount subarrays with sum k:")
    print(subarray_sum_equals_k([1, 2, 3], 3))

    print("\nLongest substring without repeating characters:")
    print(longest_substring_without_repeating(s))