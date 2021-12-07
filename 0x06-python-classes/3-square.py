#!/usr/bin/python3
''' Class Square that defines a square '''


class Square:
    def __init__(self, size):
        ''' Constructor '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        ''' area calculator '''
        return (self.__size ** 2)
