from datetime import datetime
import sys


def is_valid_date(date):
    try:
        datetime.strptime(date, '%d-%m-%Y')
        return True
    except ValueError:
        return False

with open('input.txt') as f:
    with open('output.txt', 'w') as out:
        for line in f:
            if is_valid_date(line.strip()):
                out.write(line)