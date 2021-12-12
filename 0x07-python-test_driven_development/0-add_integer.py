#!/usr/bin/python3
# doctest
def add_integer(a, b=98):
    """
    Return the result of a + b
    >>> add_integer(1, 2)
    3
    """
    if not isinstance(a, int):
        raise ValueError("a must be an integer")
    elif isinstance(a, float):
        a = int(a)
    if not isinstance(b , (int, float)):
        raise ValueError("b must be an integer")
    elif isinstance(b, float):
        b = int(b)
    return a + b
