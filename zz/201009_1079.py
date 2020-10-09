def main():
  while(True):
    characters = input().split(' ')

    for character in characters:
      print(character)
      
      if 'q' == character:
        return


if __name__ ==  '__main__':
	main()
