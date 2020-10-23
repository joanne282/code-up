def main():
    n = int(input())
    numbers = input().strip().split(' ')
    mylist = [0] * 23

    for number in numbers:
        number = int(number)
        mylist[number - 1] += 1

    for i in range(23):
        print(mylist[i], end=' ')


if __name__ == '__main__':
    main()
