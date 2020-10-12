def main():
    word = input()
    length = len(word)

    for c in word:
        length = length - 1
        value = int(c) * (10 ** length)
        print("[{}]".format(value))


if __name__ == '__main__':
    main()
