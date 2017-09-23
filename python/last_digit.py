#!/usr/bin/env python3

"""
Define a function that takes in two numbers a and b and returns the last 
decimal digit of a^b. Note that a and b may be very large!

For example, the last decimal digit of 9^7 is 9, since 9^7 = 4782969. The last 
decimal digit of (2^200)^(2^300), which has over 10^92 decimal digits, is 6.

The inputs to your function will always be non-negative integers.

Examples

>>> last_digit(4, 1)
4
>>> last_digit(4, 2)
6
>>> last_digit(9, 7)
9
>>> last_digit(10, 10 ** 10) 
0
>>> last_digit(2 ** 200, 2 ** 300)
6
"""

def last_digit(a, b):
  return 1 if b == 0 else a**(b % 4 + 4) % 10

if __name__ == '__main__':
    import doctest
    doctest.testmod()
