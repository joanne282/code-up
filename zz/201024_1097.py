def main():
    MAX = 19
    arr = [0] * MAX

    for j in range(MAX):
        arr[j] = input().split()
        # print(arr[j])
        # print(f"arr[j] len: {len(arr[j])}")

        for i in range(MAX):
            # print(f"[{i}] {arr[j][i]}")
            arr[j][i] = int(arr[j][i])

    nth = int(input())

    for n in range(nth):
        y, x = input().split()
        y, x = int(y), int(x)

        y = y - 1
        x = x - 1

        for i in range(MAX):
            if arr[y][i] == 0:
                arr[y][i] = 1
            else:
                arr[y][i] = 0

        for j in range(MAX):
            if arr[j][x] == 0:
                arr[j][x] = 1
            else:
                arr[j][x] = 0

    for j in range(MAX):
        for i in range(MAX):
            print(arr[j][i], end=' ')
        print('')


if __name__ == '__main__':
    main()
