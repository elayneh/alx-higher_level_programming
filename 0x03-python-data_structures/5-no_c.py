#!/usr/bin/python3
def no_c(my_string):
    string_chars = list(my_string)
    for char in string_chars:
        if char == 'c' or char == 'C':
            string_chars.remove(char)
    return("".join(string_chars))
