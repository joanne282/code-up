def main():
    h, b, c, s = input().split(' ')
    h, b, c, s = int(h), int(b), int(c), int(s)
    byte = b / 8

    cap = h * byte * c * s
    cap = cap / (1 << 10) / (1 << 10)
    print("{} MB".format(round(cap, 1)))


if __name__ == '__main__':
    main()
