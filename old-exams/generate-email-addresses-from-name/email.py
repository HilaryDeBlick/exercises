with open('input.txt') as f:
    with open('output.txt', 'w') as out:
        for line in f:
            name = line.strip().lower().split(' ')
            firstname = name[0]
            lastname = ''.join(name[1:])
            print(f'{firstname}.{lastname}@student.ucll.be', file=out)