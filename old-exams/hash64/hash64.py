import base64
import hashlib

def process(i):
    hash = hashlib.sha384(str(i).encode('ascii')).digest()
    return base64.b64encode(hash).decode('ascii')

with open('output.txt', 'w') as out:
    for i in range(0, 10001):
        result = process(i)
        out.write(f'{i} {result}\n')