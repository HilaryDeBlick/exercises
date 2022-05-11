def slug(name):
    parts = name.split(' ')
    first = parts[0]
    last = parts[1:]

    return "-".join(s.lower() for s in last + [first])