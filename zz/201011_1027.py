def main():
    year, month, day = input().split('.')
    year, month, day = int(year), int(month), int(day)
    print("%02d-%02d-%04d" % (day, month, year))


if __name__ == '__main__':
    main()
