#function greatest_sum(ns) that looks for the slice of ns with the greatest sum. The result should be a pair (i, j) indicating the beginning and end of the slice.
#For example, say ns == [-1, 3, 5, -10, 2]. The slice ns[1:3], i.e., [3, 5], has the greatest sum: 8. The result should therefore be (1, 3).
#make a def greatest_sum(ns) with slice_sum(pair) as the key

def greatest_sum(ns):
    def slice_sum(pair):
        i, j = pair
        return sum(ns[i:j])

    return max( [ (i, j) for i in range(0, len(ns)) for j in range(i + 1, len(ns) + 1) ], key=slice_sum )