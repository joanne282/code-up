#1087
num = int(input())
sum = 0

for i in range(num):
  i = int(i)
  sum = sum + i + 1

  if sum == num or sum>num:
    print(sum)
    break

# 1088
num = int(input())

for i in range(num+1):
  if i %3 == 0:
    continue
  else:
    print(i, end=" ")

#1089
a, d, n = input().split()
a = int(a)
d = int(d)
n = int(n)

result = (d * (n-1)) + a

print(result)