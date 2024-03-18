#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    thecopy = my_list.copy()
    if idx < 0:
        return thecopy
    if idx >= len(thecopy):
        return thecopy
    else:
        thecopy[idx] = element
        return thecopy
