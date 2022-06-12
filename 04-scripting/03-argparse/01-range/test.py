import argparse

parser = argparse.ArgumentParser(prog='git')
parser.add_argument('location')
parser.add_argument('--author')
parser.add_argument('-i', '--regexp-ignore-case', action='store_true')
parser.add_argument('--format')

# Parses sys.argv and stores parameters in args
args = parser.parse_args()

print(args)