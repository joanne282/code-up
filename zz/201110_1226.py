def main():
    lotto_numbers = input().split()
    my_numbers = input().split()

    lotto = [0] * 46

    for number in lotto_numbers:
        number = int(number)
        lotto[number] = 1
    lotto[int(lotto_numbers[-1])] -= 0.5

    score = 0
    for number in my_numbers:
        number = int(number)
        score += lotto[number]

    if score == 3:
        rank = 5
    elif score == 4:
        rank = 4
    elif score == 5:
        rank = 3
    elif score == 5.5:
        rank = 2
    elif score == 6:
        rank = 1
    else:
        rank = 0

    print(rank)


if __name__ == "__main__":
    main()
