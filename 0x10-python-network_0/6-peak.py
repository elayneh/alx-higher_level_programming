#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers """

def find_peak(list_of_integers):

    size = len(list_of_integers)
    recursive_mid = size
    mid = size // 2

    if size == 0:
        return None

    while True:
        recursive_mid = recursive_mid // 2
        if (mid < size - 1 and
                list_of_integers[mid] < list_of_integers[mid + 1]):
            if recursive_mid // 2 == 0:
                recursive_mid = 2
            mid = mid + recursive_mid // 2
        elif recursive_mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            if recursive_mid // 2 == 0:
                recursive_mid = 2
            mid = mid - recursive_mid // 2
        else:
            return list_of_integers[mid]
