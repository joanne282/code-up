def main():
    n1, n2, n3 = input().split(' ')
    n1, n2, n3 = int(n1), int(n2), int(n3)

    if n1 % 2 == 0:
        print("even")
    else:
        print("odd")

    if n2 % 2 == 0:
        print("even")
    else:
        print("odd")

    if n3 % 2 == 0:
        print("even")
    else:
        print("odd")


if __name__ == '__main__':
    main()
