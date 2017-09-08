"""

makeParts(arr, csize) given a Python list arr and chunk size (csize), 
return a list of smaller csize lists of all the original elements in
arr.

Example: if an array of size 123 is given and chunk size is 10 there will be 
13 parts, 12 of size 10 and 1 of size 3.

doctests
>>> makeParts([1, 2, 3], 1)
[[1], [2], [3]]
>>> makeParts([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3)
[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]


"""

def makeParts(arr, csize):
  return [ arr[i: i + csize] for i in range(0, len(arr), csize) ]

if __name__ == "__main__":
   import doctest
   doctest.testmod()

