def main():
    n1 = input()
    n1 = int(n1)

    if n1 > 0:
        print("plus")
    else:
        print("minus")

    if n1 % 2 == 0:
        print("even")
    else:
        print("odd")


if __name__ == '__main__':
    main()
