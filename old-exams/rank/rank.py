import json
import sys


def name(entry):
    return entry['name']

def score(entry):
    return entry['score']

#read file input.json
with open('input.json') as file:
    data = json.load(file)

data.sort(key=score, reverse=True)

#write to output.txt
with open('output.txt', 'w') as f:
    for index, entry in enumerate(data):
        rank = index + 1
        print(f'{rank} {name(entry)}', file=f)
