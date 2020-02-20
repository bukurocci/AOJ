import math

n = int(input())
count = 0

def is_prime(x):
  # 素数は2以上の数で1とその数以外で割ることができない数

  # 2は偶数だけど、素数
  if(x == 2):
    return True

  # 1と2の倍数は素数ではない
  if(x < 2 or x % 2 == 0):
    return False

  sqrt =  math.sqrt(x)
  i = 3
  
  # xが合成数だと仮定すると 2から sqrt(x) までの間の整数で割り切れる
  while(i <= sqrt):
    if(x % i == 0):
      return False
    
    i += 2

  return True

for _ in range(n):
  count += 1 if is_prime(int(input())) else 0

print(count)