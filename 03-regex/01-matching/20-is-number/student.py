import re
#also allow a .
def is_number(string):
    return re.fullmatch('[0-9]+(\.[0-9]+)?', string)