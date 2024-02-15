#!/usr/bin/python3
def raise_exception():
    try:
        where_I_am = "I'm here" + "at lane" + 42
    except TypeError as e:
        raise e
