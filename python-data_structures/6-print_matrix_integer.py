#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if not row:  # if the row is empty, skip printing anything
            continue
        for i, num in enumerate(row):
            if i != len(row) - 1:
                print("{:d}".format(num), end=" ")
            else:
                print("{:d}".format(num))
