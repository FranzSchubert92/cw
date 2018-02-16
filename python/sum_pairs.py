"""
Sum of Pairs

Given a list of integers and a single sum value, return the first two values 
(parse from the left please) in order of appearance that add up to form the sum.

sum_pairs([11, 3, 7, 5],         10)
#              ^--^      3 + 7 = 10
    == [3, 7]

sum_pairs([4, 3, 2, 3, 4],         6)
#          ^-----^         4 + 2 = 6, indices: 0, 2 *
#             ^-----^      3 + 3 = 6, indices: 1, 3
#                ^-----^   2 + 4 = 6, indices: 2, 4
#  * entire pair is earlier, and therefore is the correct answer
    == [4, 2]

sum_pairs([0, 0, -2, 3], 2)
#  there are no pairs of values that can be added to produce 2.
== None/nil/undefined (Based on the language)

sum_pairs([10, 5, 2, 3, 7, 5],         10)
#              ^-----------^   5 + 5 = 10, indices: 1, 5
#                    ^--^      3 + 7 = 10, indices: 3, 4 *
#  * entire pair is earlier, and therefore is the correct answer
    == [3, 7]
Negative numbers and duplicate numbers can and will appear.

NOTE: There will also be lists tested of lengths upwards of 10,000,000 elements. 
Be sure your code doesn't time out.

>> DocTests >>
>>> sum_pairs_hm([11, 3, 7, 5], 10)
[3, 7]
>>> sum_pairs_hm([1, 4, 8, 7, 3, 15], 8)
[1, 7]
>>> sum_pairs_hm([0, 2, 0], 0)
[0, 0]

"""

def sum_pairs(ints, s):
    """brute force version"""
    sz = len(ints)
    for i in range(sz):
        for j in range(i):
            if j < i:
                if ints[i] + ints[j] == s:
                    return [ints[j], ints[i]]

def sum_pairs_hm(ints, s):
    """using dict for memoization"""
    find_pair = {}
    for val in ints:
        pair = s - val
        if pair in find_pair:
            return [pair, val]
        else:
            find_pair[val] = pair

def sum_pairs_set(lst, s):
    """using set for memoization"""
    cache = set()
    for i in lst:
        if s - i in cache:
            return [s - i, i]
        cache.add(i)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

