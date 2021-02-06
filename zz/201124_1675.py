def main():
    sentence = input()

    for s in sentence:
        if s == " ":
            print(" ", end="")
            continue

        idx = ord(s) - 3
        if idx < 97:
            idx += ord("z") - ord("a") + 1
        print(chr(idx), end="")


if __name__ == "__main__":
    main()
