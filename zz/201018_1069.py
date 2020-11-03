def main():
    e = input()

    evaluation = {
        "A": "best!!!",
        "B": "good!!",
        "C": "run!",
        "D": "slowly~",
    }

    if e in evaluation:
        print(evaluation[e])
    else:
        print('what?')


if __name__ == '__main__':
    main()
