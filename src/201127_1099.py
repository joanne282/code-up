# 1099
list_num = [0]*10
for i in range(10):
  list_num[i] = input().split()

for j in range(10):
  for i in range(10):
    list_num[j][i] = int(list_num[j][i])

i = 1
j = 1

while(1):

  if list_num[j][i] == 2:
    list_num[j][i] = 9
    break
  
  elif list_num[j][i] == 0:
    list_num[j][i] = 9       
    i += 1
  
  elif list_num[j][i] == 1:
    j += 1
    i -= 1
    if list_num[j][i] == 1:
      break


for j in range(10):
  for i in range(10):
    print(list_num[j][i], end=" ")
  print(" ")