#in this we will see about the operations and functions of tuple
from itertools import count

Tuple_one = (1,2,3,4,5)
Tuple_two = (4,2,1,4,1)

print(Tuple_one + Tuple_two)

#we only have two methods for the tuple
#1. count() and 2.index()

print(Tuple_one.count(2))#count the number of particular number

print(Tuple_one.index(4))#tells the index of the particular element



#max(), min(), and sum()


def sum_product(input_tuple):
    sum_result = sum(input_tuple)
    product_result = 1


    for i in input_tuple:
        product_result *= i



    return sum_result, product_result

print(sum_product(Tuple_two))


