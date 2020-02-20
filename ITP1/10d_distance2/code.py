
def chebyshev_distance(x, y, n):
  m = 0

  for i in range(n):
    d = abs(x[i] - y[i])

    if(d > m):
      m = d

  return m


def minkowski_distance(x, y, p, n):
  total = 0

  for i in range(n):
    d = abs(x[i] - y[i])
    total += d ** p

  return total ** (1 / p)


n = int(input());

x = list(map(int, input().split()))
y = list(map(int, input().split()))


print("{:.7f}".format(minkowski_distance(x, y, 1, n)))
print("{:.7f}".format(minkowski_distance(x, y, 2, n)))
print("{:.7f}".format(minkowski_distance(x, y, 3, n)))
print("{:.7f}".format(chebyshev_distance(x, y, n)))




