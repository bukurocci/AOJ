import math

while True:
  n = int(input())

  # 学生の数 n = 0 の時処理を終わる（指定された終了条件）
  if(n == 0):
    break

  samples = list(map(int, input().split()))

  m = sum(samples) / n

  v = 0

  for sample in samples:
    v += (sample - m) ** 2

  v /= n

  d = math.sqrt(v)

  print("{:.6f}".format(d))

  