def main():
    n1, n2 = input().split(' ')
    n1, n2 = int(n1), int(n2)

    result = int(((not n1) and (not n2)))
    print(result)


if __name__ == '__main__':
    main()
