def main():
    n = int(input())
    numbers = input().strip().split(' ')

    for number in reversed(numbers):
        print(number, end=' ')


if __name__ == '__main__':
    main()
