def frequencies(xs):
    freq = {}
#    alternative method
#
#    for x in xs:
#       freq[x] = freq.get(x, 0) + 1
    for x in xs:
        if x not in freq:
            freq[x] = 0
        freq[x] += 1
    return freq