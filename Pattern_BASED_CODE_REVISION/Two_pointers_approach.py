#two pointers when dealing with sorted data, paris or problems where elements at two ends/in the list  need to be compared
#Pair or Triplet
#sum or equals to
#Reverse or Palindrome
#Closest to min/max


l1 = [1,2,3,4,5,6]

target = 3

#two sum on sorted list

left = 0
right = len(l1)-1

while left < right:
    s = l1[left] + l1[right]
    if s == target:
        print(left,right)
        break
    elif s < target:
        left += 1   
    else:
        right -= 1

print(l1)


