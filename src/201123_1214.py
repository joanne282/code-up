# 1214
year, mon = input().split(' ')
year = int(year)
mon = int(mon)

if(year % 4 == 0 and year % 100 == 0):
  if (mon == 2):
    print(29)
  elif (mon == 4 or mon == 6 or mon == 9 or mon == 11):
    print(30)
  else:
    print(31)

elif (year % 4 ==0 and year % 100 != 0):
  if (mon == 2):
    print(29)
  elif (mon == 4 or mon == 6 or mon == 9 or mon == 11):
    print(30)
  else:
    print(31)

else:
  if (mon == 2):
    print(28)
  elif (mon == 4 or mon == 6 or mon == 9 or mon == 11):
    print(30)
  else:
    print(31)