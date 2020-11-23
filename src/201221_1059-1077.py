# 1059
num = input()
num = int(num)
num = ~num

print(num)

# 1060
num1, num2 = input().split()
num1 = int(num1)
num2 = int(num2)

num = num1 & num2

print(num)

# 1061
num1, num2 = input().split()
num1 = int(num1)
num2 = int(num2)

num = num1 | num2

print(num)

# 1062
num1, num2 = input().split()
num1 = int(num1)
num2 = int(num2)

num = num1 ^ num2

print(num)

# 1063
num1, num2 = input().split()
num1 = int(num1)
num2 = int(num2)

if (num1>num2) == 1:
  print(num1)
else:
  print(num2)

# 1064
num1, num2, num3 = input().split()
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

if ((num1<num2)&(num1<num3)) == 1:
  print(num1)
elif ((num2<num1)&(num2<num3)) == 1:
  print(num2)
elif ((num3<num1)&(num3<num2)) == 1:
  print(num3)
elif (num1==num2==num3):
  print(num1)

# 1065
num1, num2, num3 = input().split()
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

if (num1%2) == 0:
  print(num1)
if (num2%2) == 0:
  print(num2)
if (num3%2) == 0:
  print(num3)

# 1066
num1, num2, num3 = input().split()
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

if (num1%2) == 0:
  print("even")
else:
    print("odd")

if (num2%2) == 0:
  print("even")
else:
    print("odd")

if (num3%2) == 0:
  print("even")
else:
    print("odd")

# 1067
num = input()
num = int(num)

if (num<0):
  print("minus")
else:
  print("plus")

if (num%2) == 0:
  print("even")
else:
  print("odd")

# 1068
"""
 90 ~ 100 : A
 70 ~   89 : B
 40 ~   69 : C
 0 ~   39 : D
"""

num = input()
num = int(num)

if (90<=num)&(num<=100):
  print("A")
elif (70<=num)&(num<=89):
  print("B")
elif (40<=num)&(num<=69):
  print("C")
else:
  print("D")

# 1069
"""
A : best!!!
B : good!!
C : run!
D : slowly~
나머지 문자들 : what?
"""
mon = input()
mon = str(mon)

if (mon=="A"):
  print("best!!!")
elif (mon=="B"):
  print("good!!")
elif (mon=="C"):
  print("run!")
elif (mon=="D"):
  print("slowly~")
else:
  print("what?")

# 1070
"""
12, 1, 2 : winter
  3, 4, 5 : spring
  6, 7, 8 : summer
  9, 10, 11 : fall
"""
num = input()
num = int(num)

if (num==1)|(num==2)|(num==12):
  print("winter")
elif (num==3)|(num==4)|(num==5):
  print("spring")
elif (num==6)|(num==7)|(num==8):
  print("summer")
elif (num==9)|(num==10)|(num==11):
  print("fall")

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
