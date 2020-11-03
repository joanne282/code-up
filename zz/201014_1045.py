def main():
    n1, n2 = input().split(' ')
    n1, n2 = int(n1), int(n2)

    print(n1 + n2)
    print(n1 - n2)
    print(n1 * n2)
    print(int(n1 / n2))
    print(n1 % n2)
    print("%.2f" % round(n1 / n2, 2))


if __name__ == '__main__':
    main()
