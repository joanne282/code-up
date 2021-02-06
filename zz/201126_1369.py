def main():
    n, k = input().split()
    n, k = int(n), int(k)

    for j in range(n):
        for i in range(n):
            if j == 0 or j == n - 1 or i == 0 or i == n - 1:
                print("*", end="")
            elif (j + i + 1) % k == 0:
                print("*", end="")
            else:
                print(" ", end="")
        print("")


if __name__ == "__main__":
    main()
