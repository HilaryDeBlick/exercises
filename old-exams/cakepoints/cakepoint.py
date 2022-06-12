with open('input.txt') as file:
    with open('output.txt', 'w') as out:
        for line in file:
            name, data = line.split(':')
            frac, signs = data.split(' ')
            cashed, earned = map(int, frac.split('/'))

            cashed += signs.count('-')
            earned += signs.count('+')

            out.write(f'{name}:{cashed}/{earned}\n')