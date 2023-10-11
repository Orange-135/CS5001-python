import sys
from char_freqs import CharFreqs

def main(file_name):
    cf = CharFreqs()

    try:
        f = open(file_name)
    except FileNotFoundError:
        print("Cant't find", file_name)
        return

    for line in f:
        cf.count_line(line)

        print("\nCharacter counts dictioary:")
        print(cf.char_counts)

        print("\nAs a sort list")
        print(cf.sorted_counts)

        print("\nCharacter freqs dictionary:")
        print(cf.char_freqs)

        print("\nSorted frequencies")
        for ch in cf.sorted_freqs:
            print(ch)


main(sys.argv[1])
