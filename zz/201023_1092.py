def main():
    a, b, c = input().split(' ')
    a, b, c = int(a), int(b), int(c)
    day = 1

    while not (day % a == 0 and day % b == 0 and day % c == 0):
        day += 1

    print(day)


if __name__ == '__main__':
    main()
