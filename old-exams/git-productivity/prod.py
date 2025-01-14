import re

table = {}

with open('input.txt', 'r') as f:
    for line in f:
        m = re.search(r'Author: (.*) <', line)
        if m:
            author = m.group(1)
            table[author] = table.get(author, 0) + 1

freqs = [n for _, n in table.items()]

with open('output.txt', 'w') as out:
    out.write("\n".join(f'{author}: {n}' for author, n in sorted(table.items(), key=lambda x: x[1], reverse=True)))