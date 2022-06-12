#read all grades from input.json and write id then average grade to output.txt
import json

result = {}

with open('input.json') as file:
    data = json.load(file)

    for student in data:
        id = student['id']
        grades = student['grades']
        average = round(sum(grades) / len(grades))
        result[id] = average

    with open('output.txt', 'w') as out:
        for id in sorted(result):
            out.write(f'{id} {result[id]}\n')