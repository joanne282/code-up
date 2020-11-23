def main():
    n = int(input())
    numbers = input().strip().split(' ')
    mylist = [0] * 23

    for number in numbers:
        number = int(number)
        mylist[number - 1] += 1

    for i in range(23):
        if mylist[i] > 0:
            print(i + 1)
            break


if __name__ == '__main__':
    main()
