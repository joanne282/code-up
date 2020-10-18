def main():
    w, h, b = input().split(' ')
    w, h, b = int(w), int(h), int(b)
    byte = b / 8

    image = w * h * byte
    image = image / (1 << 10) / (1 << 10)
    print("%.2f MB" % round(image, 2))


if __name__ == '__main__':
    main()
