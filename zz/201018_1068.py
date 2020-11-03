def main():
    n1 = input()
    n1 = int(n1)

    if 90 <= n1 and n1 <= 100:
        print("A")
    elif 70 <= n1 and n1 < 90:
        print("B")
    elif 40 <= n1 and n1 < 70:
        print("C")
    else:
        print("D")


if __name__ == '__main__':
    main()
