import re
def contains_no_a(string):
    return not re.search(r'a', string)
    # or return re.fullmatch('[^a]*', string)