#1284 - 암호해독

num = int(input())
chk_1 = 1
wrong = 0
cnt = 0
cnt_1 = 0

for i in range (2,num-1):
  if num%i == 0:
    chk_1 = i
    cnt += 1

chk_2 = int(num/chk_1)

for i in range (2,chk_1-1):
  if chk_1%i==0:
    cnt_1 += 1

if cnt == 2 and cnt_1 == 0:  
  print(chk_2,end=" ")
  print(chk_1)

elif cnt ==1 and cnt_1 == 0:
  if num/chk_1 == chk_2:
    print(chk_2,end=" ")
    print(chk_1)
else:
  print("wrong number")