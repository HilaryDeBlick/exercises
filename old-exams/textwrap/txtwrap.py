import textwrap

#read file input.txt
with open('output.txt', 'w') as f:
    print("\n".join(textwrap.wrap(open('input.txt').read(), 40)), file=f)
