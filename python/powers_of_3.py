"""
Powers of Three: Given a positive integer N, return the largest integer k such
that 3**k < N.

For example,

>>> largestPower(3)
0
>>> largestPower(4)
1
>>> largestPower(28)
3
>>> largestPower(80)
3
>>> largestPower(82)
4
>>> largestPower(20700)
9
>>> largestPower(10**7)
14
>>> largestPower(10**8)
16

"""

from math import ceil, log

def largestPower_v1(n):
    k = -1
    while 3**k < n:
        if 3**(k+1) >= n:
            break
        k += 1
    return k

def largestPower_v2(n):
    return int(ceil(log(n, 3)) - 1)

if __name__ == "__main__":
    import doctest
    import timeit

    for func in [largestPower_v1, largestPower_v2]:
        largestPower = func
        print("testing", func.__name__)
        out = timeit.timeit('doctest.testmod()', 
                            setup="from __main__ import doctest,largestPower", 
                            number=1000)
        print(out)
  

