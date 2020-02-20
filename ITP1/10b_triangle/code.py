import math

#a -> 辺1の長さ
#b -> 辺2の長さ
#C -> 角ab
a,b,C = list(map(int, input().split()));

#角度Cをラジアンに変更する
radC = C * math.pi / 180

# 余弦定理を使って残った辺 x を求める
x = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(radC))

#面積を求めるために高さhを求める
h = b * math.sin(radC)

# 面積をS求める
S = 0.5 * a * h

# 周の長さLを求める
L = a + b + x

print("{:.8f}".format(S))
print("{:.8f}".format(L))
print("{:.8f}".format(h))


