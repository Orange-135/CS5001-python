import sys


def main(width, height):
    for _ in range(height):
        print("*" * width)


main(int(sys.argv[1]), int(sys.argv[2]))