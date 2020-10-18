def main():
    n1, n2 = input().split(' ')
    n1, n2 = int(n1), int(n2)

    if n1 == n2:
        result = 1
    else:
        result = 0

    print(result)


if __name__ == '__main__':
    main()
