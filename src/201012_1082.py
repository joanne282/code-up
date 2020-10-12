num = input()
num = int(num,16)

for i in range(1,16):
  i = int(i)
  num1 = num * i
  print('%X*%X=%X' %(num, i, num1))