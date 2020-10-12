num1, num2 = input().split()
num1 = int(num1)
num2 = int(num2)

for i in range(num1):
  i = int(i+1)
  for j in range(num2):
    j = int(j+1)
    print("%d %d" %(i, j))