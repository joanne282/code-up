#1675 - 시저의 암호1
list_mon = str(input())
chk = len(list_mon)
list_chk = [0]*200

for i in range(chk):
  list_chk[i] = ord(list_mon[i])-3
  # print(list_chk[i])
  
  if (list_chk[i]<97):
    list_chk[i] += 26

for i in range (chk):  
  if list_chk[i] == 55:
    print(" ",end="")
  else:
    print(chr(list_chk[i]),end="")