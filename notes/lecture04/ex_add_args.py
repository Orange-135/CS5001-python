import sys

def main(args):
    print(sum([int(arg) for arg in args]))

main(sys.argv[1:])