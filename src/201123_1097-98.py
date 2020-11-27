# 1097
list_a=[[0]*19 for i in range(19)]

list_a = [[int(x) for x in input().split()] for y in range(19)]

num = int(input())

for i in range(0,num):
  chk1, chk2 = input().split()
  chk1 = int(chk1)
  chk2 = int(chk2)

  for j in range(0,19):
    if(list_a[chk1-1][j]==0):
      list_a[chk1-1][j] = 1
    else:
      list_a[chk1-1][j] = 0
  
  for j in range(0,19):
    if(list_a[j][chk2-1]==0):
      list_a[j][chk2-1] = 1
    else:
      list_a[j][chk2-1] = 0

for i in range(0,19):
  for j in range(0,19):
    if(j==18):
      print(list_a[i][j], end="\n")
    else:
      print(list_a[i][j], end=" ")



# 1098
num_h, num_w = input().split(' ')
num_n = int(input())

list_n = [[0]*10 for i in range(10)]
list_res = [[0]*10 for i in range(10)]

list_n = []
for i in range(1, 4):
  list_n.append(i * 4)
print(list_n)

list_n = [i * 4 for i in range(1, 4)]
print(list_n)

num_h = int(num_h)
num_w = int(num_w)

for i in range(0,num_n):
  num_i, num_d, num_x, num_y = input().split()
  num_i = int(num_i)
  num_d = int(num_d)
  num_x = int(num_x)
  num_y = int(num_y)


  if num_d==0:
    for j in range(0,num_i):
      list_res[num_x-1][num_y-1+j] = 1      

  elif num_d == 1:
    for j in range(0,num_i):
      list_res[num_x-1+j][num_y-1] = 1


for i in range(0,num_h):
  for j in range(0,num_w):
    if j==(num_w-1):
      print(list_res[i][j],end ="\n")
    else:
      print(list_res[i][j],end =" ")
