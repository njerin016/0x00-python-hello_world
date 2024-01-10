#!/usr/bin/python3

for number in range(0, 100):
    if number in range(0, 10):
        print(f"0{number}, ", end="")
    elif number == 99:
        print(f"{number}")
    else:
        print(f"{number}, ", end="")
