def main():
    value = int(input())
    sum = 0

    for i in range(1, value + 1):
        sum += i

        if sum >= value:
            print(sum)
            break


if __name__ == '__main__':
    main()
