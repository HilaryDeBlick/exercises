'''read input.txt and write all lines matching regex to output.txt
regex'''
import re
import sys

with open('input.txt') as f:
    with open('output.txt', 'w') as out:
        for line in f:
            if re.fullmatch(r'(0|\+32-)4[5-9][0-9]-\d{2}-\d{2}-\d{2}', line.strip()):
                out.write(line)