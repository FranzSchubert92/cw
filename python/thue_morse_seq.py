#!/usr/bin/env python3

"""
Given a positive integer n, return first n dgits of Thue-Morse sequence, as a 
string (see examples).

The Thue-Morse sequence is a binary sequence with 0 as the first element. The 
rest of the sequece is obtained by adding the Boolean (binary) complement of a 
group obtained so far.

For example:

0
01
0110
01101001
and so on...
alt

>>> thue_morse(1)
'0' 
>>> thue_morse(2)
'01' 

"""

def thue_morse(n):
    s = '01'
    while len(s) < n:
       s += ''.join(('1' if x == '0' else '0' for x in s))
    return s[:n]

def thue_morse_sub(n):
    """ generate Thue-Morse sequence using substitution system: 
        0 -> 01
        1 -> 10
    See http://mathworld.wolfram.com/Thue-MorseSequence.html"""
    pass
                
for i in range(0, 17, 2):
    print(i, thue_morse(i))

if __name__ == "__main__":
    import doctest
    doctest.testmod()

