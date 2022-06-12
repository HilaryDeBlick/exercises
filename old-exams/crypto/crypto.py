'''read each currency from jsonfile input.json and write it to output.txt'''
import json
from locale import currency
import sys

with open('input.json') as file:
    data = json.load(file)
    with open('output.txt', 'w') as out:
        for coin in data:
            currency = coin['currency']
            history = coin['history']
            minimum = min(history)
            maximum = max(history)
            current = history[-1]
            out.write(f'{currency} {minimum} {maximum} {current}\n')