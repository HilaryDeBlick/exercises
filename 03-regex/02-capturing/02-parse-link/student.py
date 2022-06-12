import re

def parse_link(string):
    match = re.fullmatch(r'<a href="(.*?)">(.*?)</a>', string)

    if match:
        return tuple( [match.group(2), match.group(1)] )
    else:
        return None