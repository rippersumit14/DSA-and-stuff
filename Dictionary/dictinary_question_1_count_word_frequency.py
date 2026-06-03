'''
Count Word Frequency
Define a function to count the frequency of words in a given list of words.

Example:

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
count_word_frequency(words)
Output:

 {'apple': 3, 'orange': 2, 'banana': 1}'''

words_list = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']

def count_word_frequency(words):
    dictionary_frequency_count = {}


    for i in words:
        if i in dictionary_frequency_count:
            dictionary_frequency_count[i] += 1
        else:
            dictionary_frequency_count[i] = 1

    return dictionary_frequency_count

print(count_word_frequency(words_list))





