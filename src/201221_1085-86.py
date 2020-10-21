# 1085
h, b, c, s = input().split()
h = int(h)
b = int(b)
c = int(c)
s = int(s)

num = float( h * b * c * s )
num = ((num/8)/1024)/1024
print("%.1f MB" %num)


# 1086
w, h, b = input().split(" ")

w = int(w)
h = int(h)
b = int(b)

num = float(w * h * b)
num = ((num/1024)/1024)/8

print("%.2f MB" %num)