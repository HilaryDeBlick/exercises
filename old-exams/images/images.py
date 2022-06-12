import imghdr

with open('output.txt', 'w') as out:
    for i in range(1,101):
        filename = f'{i}.unknown'
        extension = imghdr.what(filename)
        print(f'mv {filename} {i}.{extension}', file=out)