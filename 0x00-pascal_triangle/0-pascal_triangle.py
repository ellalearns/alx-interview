#!/usr/bin/python3
"""
contains an algorithm for generating rows of a pascal's triangle
depending on number of rows provided - 1
"""


def get_next_row(row=0, row_values=[]):
    """
    given a row in a Pascal's triangle
    return the next row
    """
    if row == 0:
        return [1]

    if row == 1:
        return [1, 1]

    next_row = [
                value if index == 0 else value + row_values[index - 1]
                for index, value in enumerate(row_values)
            ]
    next_row.append(1)

    return next_row


def pascal_triangle(n):
    """
    returns a list of lists of integers
    representing the Pascal's triangle of (n - 1) rows

    n is the number of rows plus one that the triangle has
    n will always be an int
    return an empty list if n <= 0
    """
    pascal_list = []
    if n <= 0:
        return pascal_list

    row_count = 0
    last_row = []

    while row_count < n:
        new_row = get_next_row(row_count, last_row)

        pascal_list.append(new_row)

        last_row = new_row
        row_count += 1

    return pascal_list
