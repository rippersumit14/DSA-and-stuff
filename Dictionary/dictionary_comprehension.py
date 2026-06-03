#in this we will learn about the dictionary comprehension which is that iterating the dictionary in shorter way
import random



city_name = ['Rome','London','Hawkins','France']

new_dict = {city:random.randint(20, 30) for city in city_name} #create a dictionary from a list
print(new_dict)


