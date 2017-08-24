#!/usr/bin/env python3

def caffeineBuzz(n):
    """
    caffeineBuzz() takes a non-zero integer as it's sole argument.  
    If the integer is divisible by 3, return the string "Java".  
    If the integer is divisible by 3 and 4, return the string "Coffee"
    If the integer is one of the above and is even, add "Script" to the end of 
    the string. Otherwise, return the string "mocha_missing!"

    >>> caffeineBuzz(1)
    'mocha_missing!'
    >>> caffeineBuzz(3)
    'Java'
    >>> caffeineBuzz(6)
    'JavaScript'
    >>> caffeineBuzz(12)
    'CoffeeScript'
    >>> caffeineBuzz(-2.567 * 10**56)
    'mocha_missing!'

    """

    g = lambda x: x + "Script" if n % 2 == 0 else x

    if n % 12 == 0:
        return g("Coffee")
    elif n % 3 == 0:
        return g("Java")
    else:
        return "mocha_missing!" 

if __name__ == "__main__":
    import doctest
    doctest.testmod()
