def main():
  number = int(input())
  sum = 0

  for i in range(number + 1):
    sum = sum + i

    if sum >= number:
      print(i)
      break


if __name__ ==  '__main__':
	main()
