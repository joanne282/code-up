def main():
    n, m = input().split()
    n, m = int(n), int(m)

    for j in range(m):
        for i in range(n):
            if (j == 0 or j == m - 1) and (i == 0 or i == n - 1):
                print("+", end="")
            elif j == 0 or j == m - 1:
                print("-", end="")
            elif i == 0 or i == n - 1:
                print("|", end="")
            else:
                print(" ", end="")
        print("")


if __name__ == "__main__":
    main()
