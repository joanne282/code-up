num = input()
num = int(num)
sum = 0

for i in range (num+1):
  sum = sum + i
  if sum >= num:
    print(i)
    break
    