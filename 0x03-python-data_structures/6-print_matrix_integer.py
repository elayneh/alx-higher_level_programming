#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        clm = 1
        for clm in row:
            if clm == len(row):
                print("{:d}".format(clm), end="")
            else:
                print("{:d}".format(clm), end=" ")
            clm = clm + 1
        print()
