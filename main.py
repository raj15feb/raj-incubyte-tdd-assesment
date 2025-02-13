"""
Python script for String Calculator
"""
from typing import AnyStr

MAX_VALUE = 1000

def add(string: AnyStr) -> int:
    """
    This function will extract numbers from string and then add them,
    it will return total
    """
    i = 0
    num_total = 0
    num = ''
    if len(string) == 0:
        return 0
    while i < len(string):
        if string[i] == '-':
            raise Exception("Negative Numbers are not allowed")
        if string[i].isnumeric():
            num += string[i]
        else:
            if num and int(num) <= MAX_VALUE:
                num_total += int(num)
                num = ''
        i += 1
    if num and int(num) <= MAX_VALUE:
        num_total += int(num)
    return num_total
    
