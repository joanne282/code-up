# 1018
time = input()
print(time)

# 1019
day = input()
list_day = day.split('.')
arr = len(list_day[0])
arr1 = len(list_day[1])
arr2 = len(list_day[2])

if(arr == 4 and arr1 == 1 and arr2 == 1):
  print(list_day[0] + '.0' + list_day[1] + '.0' + list_day[2])

elif (arr == 4 and arr1 == 2 and arr2 == 1):
  print(list_day[0] + '.' + list_day[1] + '.0' + list_day[2])

elif (arr == 4 and arr1 == 1 and arr2 == 2):
  print(list_day[0] + '.0' + list_day[1] + '.' + list_day[2])

elif (arr == 4 and arr1 == 2 and arr2 == 2):
  print(list_day[0] + '.' + list_day[1] + '.' + list_day[2])

elif(arr == 2 and arr1 == 1 and arr2 == 1):
  print('00' + list_day[0] + '.0' + list_day[1] + '.0' + list_day[2])

elif (arr == 2 and arr1 == 2 and arr2 == 1):
  print('00' + list_day[0] + '.' + list_day[1] + '.0' + list_day[2])

elif (arr == 2 and arr1 == 1 and arr2 == 2):
  print('00' + list_day[0] + '.0' + list_day[1] + '.' + list_day[2])

else:
  print('00' + list_day[0] + '.' + list_day[1] + '.' + list_day[2])

# 1020
lis = input()
list_lis = lis.split('-')
print(list_lis[0]+list_lis[1])

# 1021
mon = input()
print(mon)

# 1022
mon = input()
print(mon)

# 1023
num = input()
list_num = num.split('.')
print(list_num[0])
print(list_num[1])

# 1024
mon = input()
list_mon = mon.split()
list_mon = list(mon)
arr = len(list_mon)

for i in list_mon:
  print("'" + i + "'")

# 1025
num = input()
list_num = list(num)

print('['+ list_num[0] + '0000]')
print('['+ list_num[1] + '000]')
print('['+ list_num[2] + '00]')
print('['+ list_num[3] + '0]')
print('['+ list_num[4] + ']')

# 1026
time = input()
list_time = time.split(':')
if list_time[1]!='00':
  print(list_time[1])
else:
  print('0')

# 1027
day = input()
list_day = day.split(".")

arr = len(list_day[0])
arr1 = len(list_day[1])
arr2 = len(list_day[2])

if arr == 4 and arr1 == 2 and arr2 == 2:
  print(list_day[2] + '-' + list_day[1] + '-' + list_day[0])

elif arr == 4 and arr1 == 1 and arr2 == 1:
  print('0' + list_day[2] + '-0' + list_day[1] + '-' + list_day[0])

elif arr == 4 and arr1 == 1 and arr2 == 2:
  print(list_day[2] + '-0' + list_day[1] + '-' + list_day[0])

elif arr == 4 and arr1 == 2 and arr2 == 1:
  print('0' + list_day[2] + '-' + list_day[1] + '-' + list_day[0])

elif arr == 2 and arr1 == 2 and arr2 == 2:
  print(list_day[2] + '-' + list_day[1] + '-00' + list_day[0])

elif arr == 2 and arr1 == 1 and arr2 == 2:
  print(list_day[2] + '-0' + list_day[1] + '-' + list_day[0])

else:
  print('0' + list_day[2] + '-' + list_day[1] + '-00' + list_day[0])