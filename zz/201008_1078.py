def main():
  number = int(input())
  sum = 0

  for i in range(number + 1):
    if i % 2 == 0:
      sum = sum + i

  print(sum)


if __name__ ==  '__main__':
	main()