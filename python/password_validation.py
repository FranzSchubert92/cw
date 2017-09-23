#!/usr/bin/env python3

"""
Write a regex that will validate a password according to the following criteria:

    At least six characters long
    contains a lowercase letter
    contains an uppercase letter
    contains a number
    Valid passwords will only be alphanumeric characters.

>>> validate_password("fjd3IR9")
True
>>> validate_password("ghdfj32")
False

"""
import re

def validate_password(s):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.{6,})"
    checker = re.compile(pattern)
    m = checker.match(s)
    #print(m)
    return bool(m)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

