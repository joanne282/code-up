# 1090
a, r, n = input().split()
a = int(a)
r = int(r)
n = int(n)

result = a * (r**(n-1))

print(result)

# 1091
a, m, d, n = input().split()
a = int(a)
m = int(m)
d = int(d)
n = int(n)

for i in range(n-1):
  a = ((a * m) + d)

print(a)

# 1092
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
day = 1

done = a * b * c

for i in range (done+1):
  if (day%a!=0) or (day%b!=0) or (day%c!=0):
    day = day + 1

print(day)

# 1093
num = int(input())
list_num = [0]*24

list_cnt = input().split()

long = len(list_cnt)
for i in range(0,long):
  list_cnt[i] = int(list_cnt[i])

for i in list_cnt:
  list_num[i] = list_num[i]+ 1

for i in range(1,24):
  if i==24:
    print(list_num[i],end="\n") 
  else:
    print(list_num[i],end=" ")


1094
num1 = int(input())
list_num = input().split()
list_num.reverse()

for i in list_num:
  print(i, end=" ")

# 1095
num1 = int(input())
list_num = input().split()
chk = num1

for i in list_num:
  i = int(i)

  if (i>=chk):
    continue
  else:
    chk = i

print(chk)

# 1096
play = int(input())
list_num = [[0] * 19 for i in range(19)]

for i in range (0,play):
  num1, num2 = input().split(' ')
  num1 = int(num1)
  num2 = int(num2)
  list_num[num1-1][num2-1] = 1

for k in range(0,19):
  for j in range(0,19):
    if j==18:
      print(list_num[k][j],end="\n")
    else:
      print(list_num[k][j],end=" ")