def main():
    a, r, n = input().split(' ')
    a, r, n = int(a), int(r), int(n)

    print(a * r ** (n - 1))


if __name__ == '__main__':
    main()
