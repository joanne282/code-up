# 1283
money = int(input())
money_chk = money
total = int(0)

day = int(input())
list_per = input().split()

for i in list_per:
  i = int(i)
  money_chk = money_chk + (money_chk * (i/100))

total = money_chk - money

if total == 0:
  print("0")
  print("same")
elif total<0:
  print("%.0f"%total)
  print("bad")
else:
  print("%.0f"%total)
  print("good")