#in this we have to find even and odd

from array import array

arr1 = array("i", [1,2,3,4,5,6])

even = 0
odd = 0

for item in arr1:
    if item % 2 == 0:
        even += 1
    else:
        odd += 1

arr2 = array("i", [even, odd])
print(arr2)

#the time complexity of this program will be o(n)
#and the space complexity will be o(n)

def pair_sum_sequence(n):
    total = 0
    for i in n:
        total = total + pari_sum(i, i+1)
    return total

def pari_sum(a, b):
    return  a + b



