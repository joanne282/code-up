def main():
    n1, n2 = input().split(' ')
    n1, n2 = float(n1), float(n2)

    results = [0] * 10
    results[0] = n1 + n2
    results[1] = n2 + n1
    results[2] = n1 - n2
    results[3] = n2 - n1
    results[4] = n1 * n2
    results[5] = n2 * n1
    results[6] = n1 / n2
    results[7] = n2 / n1
    results[8] = n1 ** n2
    results[9] = n2 ** n1

    max_result = max(results)
    print("%.6f" % max_result)


if __name__ == '__main__':
    main()
