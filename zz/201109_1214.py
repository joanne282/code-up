def main():
    year, month = input().split()
    year, month = int(year), int(month)

    cal = [0] * 13
    cal[1] = 31
    cal[2] = 28
    cal[3] = 31
    cal[4] = 30
    cal[5] = 31
    cal[6] = 30
    cal[7] = 31
    cal[8] = 31
    cal[9] = 30
    cal[10] = 31
    cal[11] = 30
    cal[12] = 31

    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        cal[2] += 1

    day = cal[month]
    print(day)


if __name__ == '__main__':
    main()
