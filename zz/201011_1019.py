def main():
    year, month, day = input().split('.')
    year, month, day = int(year), int(month), int(day)
    print("%04d.%02d.%02d" % (year, month, day))


if __name__ == '__main__':
    main()
