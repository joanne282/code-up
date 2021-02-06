# 1205
a, b = input().split(' ')
a = int(a)
b = int(b)
list_chk = [0]*6

list_chk[0] = plus = a + b
list_chk[1] = minues = abs(a - b)
list_chk[2] = multi = a * b
list_chk[3] = division = abs(a / b)
list_chk[4] = square_a = a**b
list_chk[5] = square_b = b**a

chk = int(0)

for i in list_chk:
  if(i >= chk):
    chk = i

print("%.6f"%chk)