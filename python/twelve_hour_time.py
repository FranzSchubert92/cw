#!/usr/bin/env python3

"""

"""
from datetime import datetime

def to12hourtime(t):
    return datetime.strptime(t,'%H%M').strftime('%I:%M %p').lstrip('0').lower()

if __name__ == '__main__':
   import doctest
   doctest.testmod()

