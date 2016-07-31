import re
import collections as c

def word_stats(filename, n):
    counts_dict = c.defaultdict(int)

    with open(filename) as nf:
        words = re.findall( r"[a-zA-Z']+", nf.read().lower() )

    for word in words:
            counts_dict[word] += 1

    return sorted(counts_dict.items(), key = lambda item: item[1], reverse = True)[:n]

    # for n in range(0, n):
    #     print("{}, {}".format(counts_sorted[n][0], counts_sorted[n][1]))



# Use Conter :
