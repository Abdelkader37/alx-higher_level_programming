#!/usr/bin/python3
def element_at(my_list, idx):
    i = idx
    if i < 0:
        return None
    if i >= len(my_list):
        return None
    else:
        return my_list[i]
