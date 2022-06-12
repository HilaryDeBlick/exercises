#def fix header that replaces al lines starting with # in = # in == and so on
import re
import sys

def fix_header(line):
    def replace(match):
        return "=" * len(match.group(1)) + match.group(2)
    return re.sub(r'^(#+)(.*)', replace, line)


def fix_bullet_point(line):
    def replace(match):
        indent = match.group(1)
        text = match.group(2)
        return "*" * (len(indent) // 2) + '*' + text
    return re.sub(r'^( *)\*(.*)', replace, line)

with open('input.md', 'r') as f:
    with open("output.txt", "w") as output:
        for line in f:
            line = fix_header(line)
            line = fix_bullet_point(line)
            print(line, end='', file=output)