def main():
    value = int(input())
    i = 1

    while i <= value:
        if i % 3 != 0:
            print(i)
        i += 1


if __name__ == '__main__':
    main()
