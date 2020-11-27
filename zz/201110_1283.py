def main():
    init_amount = int(input())
    day = int(input())
    rates = input().split()

    amount = init_amount
    for rate in rates:
        rate = int(rate)
        amount *= (100 + rate) * 0.01

    money = "%.0f" % (amount - init_amount)
    money = int(money)
    print(money)

    if money > 0:
        print("good")
    elif money == 0:
        print("same")
    elif money < 0:
        print("bad")


if __name__ == "__main__":
    main()
