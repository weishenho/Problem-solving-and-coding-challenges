'''
items = (
    ("map", 9, 150), ("compass", 13, 35), ("water", 153, 200), ("sandwich", 50, 160),
    ("glucose", 15, 60), ("tin", 68, 45), ("banana", 27, 60), ("apple", 39, 40),
    ("cheese", 23, 30), ("beer", 52, 10), ("suntan cream", 11, 70), ("camera", 32, 30),
    ("t-shirt", 24, 15), ("trousers", 48, 10), ("umbrella", 73, 40),
    ("waterproof trousers", 42, 70), ("waterproof overclothes", 43, 75),
    ("note-case", 22, 80), ("sunglasses", 7, 20), ("towel", 18, 12),
    ("socks", 4, 50), ("book", 30, 10))
'''

#

import numpy as np

def dp(items, limit):
    table = np.zeros((items.shape[0] + 1, limit + 1))
    for j in range(1, table.shape[0]):
        wt = items[j-1]
        for w in range(1, table.shape[1]):
            if wt > w:
                table[j][w] = table[j-1][w]
            else:
                table[j][w] = max(table[j-1][w], table[j-1][w-wt] + wt)


    result = []
    removeindex = []
    w = limit
    for j in range(items.shape[0], 0, -1):
        was_added = table[j][w] != table[j-1][w]

        if was_added:
            wt= items[j-1]
            result.append(items[j-1])
            removeindex.append(j-1)
            w -= wt

    items = np.delete(items, removeindex)

    return result, items


limit = 12
items = np.array([2,2,3,3,3,3,4,4,4,6,7,7])
items = items[::-1]


while items.sum() > 12:
    result, items = dp(items, limit)
    print(result, items, sum(result))
    print()