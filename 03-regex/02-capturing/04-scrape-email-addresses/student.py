import re

def scrape_email_addresses(string):
    return re.findall(r'[\w\.-]+@[\w\.-]+', string)