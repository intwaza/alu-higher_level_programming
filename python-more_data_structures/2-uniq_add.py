#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_elements = set(my_list)
    total = 0
    for num in unique_elements:
        total += num
    return total
