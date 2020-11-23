# 1071
num = input()
list_num = num.split(" ")

for i in list_num:
  i = int(i)
  if i == 0:
    break
  print(i)

# 1072
num = input()
num = int(num)

num1 = input()
list_num1 = num1.split(" ")

for i in list_num1:
  print(i)

# 1073
num = input()
list_num = num.split(" ")

for i in list_num:
  if i=="0":
    break
  else:
    print(i)

# 1074
num = input()
num = int(num)

for i in range (0, num):
  i = int(i)
  i = num

  print(i)
  num = num - 1

# 1075
num = input()
num = int(num)

for i in range (0, num):
  i = int(i)
  i = num - 1

  print(i)
  num = num - 1

# 1076
num = input()
num = ord(num) 

for i in range (97, num+1):
  i = int(i)

  if i == num:
    print(chr(i), end=" ")
    break
  else:
    print(chr(i), end=" ")
    i = i + 1


# 1077

num = input()
num = int(num)

for i in range(0,num+1):
  i = int(i)

  print(i)