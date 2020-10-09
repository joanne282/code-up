num = input()
num = int(num)
sum = 0
chk = 0

for i in range (num+1):
  sum = sum + i
  if sum < num:
    chk = i+1
    exit

print(chk)
