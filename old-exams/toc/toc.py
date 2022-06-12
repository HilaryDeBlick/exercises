import sys
import re


with open('input.asciidoc', 'r') as f:
    data = f.read()
    with open('output.txt', 'w') as f2:
        for id, sec, title in re.findall(r'\[#(.*?)\]\s*(=+) (.*)', data):
            depth = len(sec)
            bullets = "*" * depth
            link = f'<<{id},{title}>>'
            print(f'{bullets} {link}', file=f2)
