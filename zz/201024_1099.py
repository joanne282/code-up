def main():
    MAX = 10
    arr = [0] * MAX

    for j in range(MAX):
        arr[j] = input().split()

        for i in range(MAX):
            arr[j][i] = int(arr[j][i])

    y = 1
    x = 1
    while(True):
        if arr[y][x] == 0:
            arr[y][x] = 9
        if arr[y][x] == 2:
            arr[y][x] = 9
            break

        if arr[y][x + 1] != 1:
            x += 1
            continue

        if arr[y + 1][x] != 1:
            y += 1
            continue

        break

    for j in range(MAX):
        for i in range(MAX):
            print(arr[j][i], end=' ')
        print('')


if __name__ == '__main__':
    main()
