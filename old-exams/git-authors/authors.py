#read input.txt filter author names, name can only appear once write to file alphabetically
import re

authors = set()

with open('input.txt', 'r') as f:
    for line in f:
        m = re.search(r'Author: (.*) <', line)
        if m:
            authors.add(m.group(1))

with open('output.txt', 'w') as out:
    out.write("\n".join(sorted(list(authors))))