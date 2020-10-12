def main():
    n, m = input().split(' ')
    n, m = int(n), int(m)

    for j in range(1, n + 1):
        for i in range(1, m + 1):
            print("{} {}".format(j, i))


if __name__ == '__main__':
    main()
