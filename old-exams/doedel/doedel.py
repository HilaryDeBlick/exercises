import csv
from collections import Counter

counter = Counter()

with open('input.csv') as file:
    data = csv.DictReader(file)
    for line in data:
        for key in line.keys():
            if key != 'name' and line[key] == 'yes':
                counter[key] += 1
    
sorted_by_count = sorted(counter.items(), key=lambda p: p[1], reverse=True)

with open('output.txt', 'w') as out:
    for date, votes in sorted_by_count:
        print(f'{date} {votes}', file=out)