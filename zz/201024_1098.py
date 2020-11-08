def main():
    h, w = input().split()
    h, w = int(h), int(w)

    arr = [0] * h

    for j in range(h):
        arr[j] = [0] * w

    nth = int(input())

    for n in range(nth):
        l, d, y, x = input().split()
        l, d, y, x = int(l), int(d), int(y), int(x)

        y = y - 1
        x = x - 1

        for i in range(l):
            if d == 0:
                arr[y][x + i] = 1
            elif d == 1:
                arr[y + i][x] = 1

    for j in range(h):
        for i in range(w):
            print(arr[j][i], end=' ')
        print('')


if __name__ == '__main__':
    main()
