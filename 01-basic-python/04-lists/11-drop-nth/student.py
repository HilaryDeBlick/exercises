# using +
def drop_nth(xs,n):
    return xs[:n] + xs[n+1:]

# using * (like ... spread in js)
def drop_nth(xs,n):
    return [*xs[:n], *xs[n+1:]]