#Given a string
#vowels
#We have to reverse the vowels

def reverse_vowels(s):

    vowels = "aeiouAEIOU"

    # convert string to list
    chars = list(s)


    left = 0
    right = len(chars) - 1

    # write your logic here
    while left < right:
        if chars[left] in vowels and chars[right] in vowels:
            chars[left] = chars[right]
        left += 1
        right -= 1

    return "".join(chars)


# TEST
print(reverse_vowels("hello"))