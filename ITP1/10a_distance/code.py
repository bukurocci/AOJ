from math import sqrt

xy = list(map(float, input().split()))

a = xy[0:2]
b = xy[2:4]

length = sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)

print("{:.8f}".format(length))