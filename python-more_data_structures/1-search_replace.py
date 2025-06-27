#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Create a new list replacing all occurrences of search with replace
    new_list = [replace if x == search else x for x in my_list]
    return new_list
