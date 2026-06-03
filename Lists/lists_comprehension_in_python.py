#in this we will learn about the list comprehension in python
#if a new list is created using a previous list then that concept in python is known as the list comprehension

prev_list = [-1,-2,-1,1,2,3]
new_list = []
for i in prev_list:
    multiply_by_2 = i * 2
    new_list.append(multiply_by_2)

print(new_list)

#to make this code short we will use the concept of list comprehension
#new_item = [new_item for item in list]

new_list_comprehension = [i * 2 for i in prev_list]
print(new_list_comprehension)

#conditional list comprehension
#new_list = [new_item for item in list if condition]


condition_list = [i for i in prev_list if i > 0]
print(condition_list)


sentence = "My name is sumit"

def is_consonant(letter):
    vowels = 'aeiou'
    return letter.isalpha() and letter.lower() not in vowels #isalpha() check there are only letters in the given string

consonants = [i for i in sentence if is_consonant(i)]
print(consonants)






