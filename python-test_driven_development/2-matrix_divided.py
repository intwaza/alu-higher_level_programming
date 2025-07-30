#!/usr/bin/python3
"""
Module that contains matrix_divided function.
This module provides a function to divide all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.
    
    Args:
        matrix: list of lists of integers or floats
        div: number (integer or float) to divide by
    
    Returns:
        list: new matrix with all elements divided by div, rounded to 2 decimal places
    
    Raises:
        TypeError: if matrix is not a list of lists of integers/floats
        TypeError: if rows have different sizes
        TypeError: if div is not a number
        ZeroDivisionError: if div is zero
    """
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"
    
    # Check if matrix is a list
    if not isinstance(matrix, list):
        raise TypeError(error_msg)
    
    # Check if matrix is not empty
    if len(matrix) == 0:
        raise TypeError(error_msg)
    
    # Check if each element is a list and contains only int/float
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(error_msg)
        if len(row) == 0:
            raise TypeError(error_msg)
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(error_msg)
    
    # Check if all rows have the same size
    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
    
    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    # Check if div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    # Create new matrix with divided elements
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)
    
    return new_matrix
