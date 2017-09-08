"""
eratosthenes_sieve module

doctests
>>> is_prime(2)
True
>>> is_prime(3)
True
>>> is_prime(4)
False
>>> is_prime(1300153)
True
"""

def is_prime(num):
    return num in set(sieve(num))
    
def sieve(n):
    """Sieve of Eratosthenes; generates primes from 2 to n
    """
    composites = set()
    for i in range(2, n+1):
        if i not in composites:
            yield i
            composites.update(range(i*i, n+1, i))

if __name__ == "__main__":
    import doctest
    doctest.testmod()

