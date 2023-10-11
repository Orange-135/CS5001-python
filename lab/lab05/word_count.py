def main():

    filename = input("Enter the file name: ")
    try:
        out = open(filename, "r")
    except Exception:
        print(f"Can't open {filename}")
        return

    file = out.read()
    word = len(file.split())
    print(f"Word:", word)

    char_nospace = file.replace(" ", "").replace("/n", "")
    print("Characters:", len(char_nospace))

    char_alphanumberic = 0
    for char in file:
        if char.isalnum():
            char_alphanumberic += 1
    print("Letters & numbers:", char_alphanumberic)

main()
