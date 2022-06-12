import json

with open('input.json') as file:
    students = json.load(file)

with open('output.txt', 'w') as out:
    print('<students>', file=out)
    for student in students:
        id, grades = student['id'], student['grades']
        formatted_grades = ''.join(f'<grade>{grade}</grade>' for grade in grades)
        print(f'<student id="{id}"><grades>{formatted_grades}</grades></student>', file=out)
    print('</students>', file=out)