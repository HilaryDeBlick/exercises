#write to ouput.txt
with open('output.txt', 'w') as f:
    for i in range(0, 10000 + 1):
        first = str(i).rjust(10)
        second = bin(i).rjust(20)
        third = hex(i).rjust(10)
        print(f'{first}{second}{third}', file=f)