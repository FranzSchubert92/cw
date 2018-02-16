
from collections import Counter

def find_missing(seq):
    """ returns missing number in arithmetic sequence """
    diffs = [seq[i] - seq[i-1] for i in range(1, len(seq))]
    counts = Counter(diffs).most_common()
    mode = counts[0][0]
    odd = counts[-1][0]
    return seq[diffs.index(odd)] + mode
