#!/usr/bin/python3

def no_c(my_string):
    result = ""
    for letter in my_string:
        if (letter.lower() == "c" or letter.upper() == "C"):
            continue
        result += letter

    print(result)

