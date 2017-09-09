"""
Demonstration of mutual recursion using Douglas Hofstadter's Male and Female
functions. See "https://rosettacode.org/wiki/Mutual_recursion#Python".

Output:
[1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7, 8, 8, 9, 9, 10, 11, 11, 12, ...
[0, 0, 1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 7, 8, 9, 9, 10, 11, 11, 12, ...

"""

def F(n): return 1 if n == 0 else n - M(F(n-1))
def M(n): return 0 if n == 0 else n - F(M(n-1))

sz = 30
print([ F(n) for n in range(sz) ])
print([ M(n) for n in range(sz) ])

