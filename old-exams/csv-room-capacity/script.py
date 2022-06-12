'''read exam-shedule.csv make location table with key (date, daytime) sort alphabetically and write it to output.txt'''
import csv
import sys

result = {}

with open('exam-schedule.csv') as file:
    data = csv.DictReader(file)

    for row in data:
        location = row['Lokaal'].strip()
        date = row['Datum'].strip()
        daypart = row['Dagdeel'].strip()

        if not location or not date or not daypart:
            print(f'Error in row: {row}')
            sys.exit(-1)

        loctable = result.setdefault(location, {})
        key = (date, daypart)
        loctable[key] = loctable.get((date, daypart), 0) + 1

locations = sorted(result.keys())

with open('output.txt', 'w') as file:
    for location in locations:
        table = result[location]
        cap = max(table.values())
        file.write(f'{location} {cap}\n')