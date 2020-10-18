def main():
    n1, n2, n3 = input().split(' ')
    n1, n2, n3 = int(n1), int(n2), int(n3)

    result1 = n1 if n1 < n2 else n2
    result2 = result1 if result1 < n3 else n3

    print(result2)


if __name__ == '__main__':
    main()
