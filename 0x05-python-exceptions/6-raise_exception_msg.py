#!/usr/bin/python3
def raise_exception_msg(message=""):
    try:
        result = noName
    except NameError:
        raise NameError(f"{message}")
