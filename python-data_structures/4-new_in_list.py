#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # Create a copy of the original list
    new_list = my_list[:]
    
    # Check if index is valid
    if 0 <= idx < len(new_list):
        new_list[idx] = element
    
    return new_list
