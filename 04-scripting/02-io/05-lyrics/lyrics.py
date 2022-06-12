#!/usr/bin/env python
import urllib.request
import json
import sys
import re

import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context


def to_url(string):
    return re.sub(' ', '%20', string)

artist, title = sys.argv[1:]
title = to_url(title)
artist = to_url(artist)

url = f"https://api.lyrics.ovh/v1/{artist}/{title}"

with urllib.request.urlopen(url) as input:
    data = json.loads(input.read())
    print(data['lyrics'])