def main():
    n1, n2, n3 = input().split(' ')
    n1, n2, n3 = int(n1), int(n2), int(n3)

    print(n1 + n2 + n3)

    mean = (n1 + n2 + n3) / 3
    print("%.1f" % round(mean, 1))


if __name__ == '__main__':
    main()
