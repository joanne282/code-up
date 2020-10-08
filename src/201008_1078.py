num = input()
num = int(num)
sum = 0

if num > 100 :
    exit

for i in range(num+1):
    if i%2 == 0 :
        sum = sum + i
    
print(sum)