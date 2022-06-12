#!/usr/bin/env python
import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as response:
    print(response.read().decode('utf-8'))