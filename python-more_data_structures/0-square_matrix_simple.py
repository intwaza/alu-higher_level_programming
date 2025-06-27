#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix with squared values
    new_matrix = []
    for row in matrix:
        new_row = [x ** 2 for x in row]
        new_matrix.append(new_row)
    return new_matrix
