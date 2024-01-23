#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    for number in my_list:
        if number % 2 == 0:
            print("{} is divisible by 2".format(number))
        else:
            print("{} is not divisible by 2".format(number))
