#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    elif 0 <= idx < len(my_list):
        return my_list[idx]
    else:
        idx >= len(my_list)
        return None
