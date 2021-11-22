#!/usr/bin/python3
def no_c(my_string):
    str_chars = list(my_string)
    for char in str_chars:
        if char == 'c' or char == 'C':
            str_chars.remove(char)
    return("".join(str_chars))
