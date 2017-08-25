#!/usr/bin/env python3

import array

"""
implement classic stack data structure using python array library

tests
>>> s = Stack()
>>> s.push(1)
>>> s.isEmpty()
False
>>> s.peek()
1
>>> s.pop()
>>> s.isEmpty()
True
>>> s.pop()
None

"""

class Stack:

    def __init__(self, type_code='i'): 
        """ Constructor. Default type_code is signed integer """
        self.items = array.array(type_code)

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    import doctest
    doctest.testmod()


