def main():
    value = int(input(), 16)

    for i in range(1, 16):
        result = value * i
        print("%X*%X=%X" % (value, i, result))


if __name__ == '__main__':
    main()
