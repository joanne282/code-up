def main():
    alpha = input()
    end = ord(alpha)
    start = ord('a')

    while start <= end:
        print(chr(start))
        start += 1


if __name__ == '__main__':
    main()
