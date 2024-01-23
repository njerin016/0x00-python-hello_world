#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:
        return None
    max_number = my_list[0]
    for number in my_list[1:]:
        if number > max_number:
            max_number = number

    return max_number
