# collect_links(string) that receives an html document and collects all hrefs from a elements
import re

def collect_links(string):
    return re.findall(r'<a href="(.*?)">', string)