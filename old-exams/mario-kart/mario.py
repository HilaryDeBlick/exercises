NPARTICIPANTS=100
TOP=10

with open('input.txt') as file:
    lines = [ line.strip() for line in list(file) ]

races = [lines[i:i+NPARTICIPANTS] for i in range(0, len(lines), NPARTICIPANTS)]

scores = {}

for race in races:
    for name, score in zip(race, range(NPARTICIPANTS, 0, -1)):
        if name not in scores:
            scores[name] = 0
        scores[name] += score

#sort scores from highest score desc
top_n = sorted(scores.items(), key=lambda x: x[1], reverse=True)[0:TOP]

with open('output.txt', 'w') as out:
    for name, score in top_n:
        print(name, file=out)