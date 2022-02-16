def contains_duplicates(xs):
    for x in range(len(xs)):
        for y in range(x + 1,len(xs)):
            if xs[x] == xs[y]:
                return True
    
    return False