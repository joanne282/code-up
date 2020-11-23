def main():
    n = int(input())

    mylist = [0] * 19

    for i in range(19):
        mylist[i] = [0] * 19

    for i in range(n):
        x, y = input().strip().split(' ')
        x, y = int(x), int(y)
        mylist[x - 1][y - 1] = 1

    for j in range(19):
        for i in range(19):
            print(mylist[j][i], end=' ')
        print('')


if __name__ == '__main__':
    main()
