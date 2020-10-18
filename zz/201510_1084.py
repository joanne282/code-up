def main():
    n1, n2, n3 = input().split(' ')
    n1, n2, n3 = int(n1), int(n2), int(n3)
    count = 0

    for h in range(n1):
        for j in range(n2):
            for i in range(n3):
                count += 1
                print("{} {} {}".format(h, j, i))

    print(count)


if __name__ == '__main__':
    main()
