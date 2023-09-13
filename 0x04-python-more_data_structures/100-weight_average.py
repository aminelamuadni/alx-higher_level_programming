#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    sum_of_products = sum([a*b for a, b in my_list])
    sum_of_weights = sum([b for _, b in my_list])

    return sum_of_products / sum_of_weights
