n = int(input())
min = int(input()) #一番最初の値を0からj-1までの最小値と仮置きする
maxp = -10 ** 9 #制約上の最小利益 - 1

for _ in range(n-1):
  value = int(input())

  p = value - min
  maxp = p if maxp < p else maxp

  if(min > value):
    min = value

print(maxp)