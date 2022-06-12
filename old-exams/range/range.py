#write to ouput.txt
with open('output.txt', 'w') as f:
    for i in range(1, 1000**2 + 1):
        print (i, file=f)