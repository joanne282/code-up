import math


def main():
    n = input()
    n = int(n)
    value = []

    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            n = int(n / i)
            value.append(i)

    if n != 1:
        value.append(n)

    if len(value) == 2:
        print("{} {}".format(value[0], value[1]))
    else:
        print("wrong number")


if __name__ == "__main__":
    main()
