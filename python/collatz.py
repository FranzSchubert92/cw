"""
collatz(n) starts a Collatz sequence from n;

doctests
>>> collatz(4)
'4->2->1'
>>> collatz(3)
'3->10->5->16->8->4->2->1'

"""

def collatz(n):
    seq = [n]
    while seq[-1] > 1:
        if seq[-1] % 2 == 0:
            seq.append( seq[-1] // 2 )
        else:
            seq.append( 3 * seq[-1] + 1 )
    return "->".join(str(x) for x in seq)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

