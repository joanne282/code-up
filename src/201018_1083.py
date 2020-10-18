num = input()
num = int(num)

for i in range(1,10):
  if(i == num + 1):
    break

  elif(i%3 ==0 ):
    print("X",end=" ")
  
  else:
    print(i, end=" ")