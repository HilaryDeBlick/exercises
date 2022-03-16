import re

def only_digits(string):
    return re.fullmatch('(a|i|u|e|o)*', string)
