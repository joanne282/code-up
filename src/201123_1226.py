# 1226
list_num = input().split(' ')
for i in list_num:
  i = int(i)

list_chk = input().split(' ')
for i in list_chk:
  i = int(i)

cnt = int(0)
count = int(0)

for i in range(0,6):
  for j in list_chk:
    if list_num[i]==j :
      cnt += 1

if cnt == 6:
  print(1)
elif cnt == 5:
  for i in list_chk:
    if list_num[6] == i:
      count = 1
  if count == 1:
    print(2)
  else:
    print(3)

elif cnt == 4:
  print(4)
elif cnt == 3:
  print(5)
else:
  print("0")