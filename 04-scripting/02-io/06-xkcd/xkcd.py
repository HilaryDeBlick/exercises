#!/usr/bin/env python
from PIL import Image
import urllib.request
import json
import sys
import re

'''fetch data from https://xkcd.com/{n}/info.0.json'''
def fetch_data(n):
    if n:
        url = f'http://xkcd.com/{n}/info.0.json'
    else:
        url = 'http://xkcd.com/info.0.json'
    
    with urllib.request.urlopen(url) as stream:
        data = stream.read().decode('utf-8')

    return json.loads(data)

def fetch_image(url):
    with urllib.request.urlopen(url) as stream:
        return Image.open(stream)

data = fetch_data(None if len(sys.argv) == 1 else int(sys.argv[1]))

for key, value in data.items():
    print(f'{key}: {value}')

fetch_image(data['img']).show()
