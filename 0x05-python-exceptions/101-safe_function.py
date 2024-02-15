#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        outcome = fct(*args)
        return (outcome)
    except Exception as e:
        sys.stderr.write("Exception: {}\n".format(e))
        return (None)
