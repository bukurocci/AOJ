a, b = list(map(int, input().split()))

def gcd(a, b):

  # a % b の余りの最大公約数が a, bの最大公約数と等しいことを利用するので
  # a > b である必要がある
  if(a > b):
    a, b = b, a

  while(b > 0):
    r = a % b
    a = b
    b = r

  return a


print(gcd(a, b))
