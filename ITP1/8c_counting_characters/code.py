import sys, string

# 標準有力を全て読んで、改行でリストに変換するそのあとリストを一つずつlowercaseに変換して、左右の空白文字を消す
text = "".join(s.lower().strip() for s in sys.stdin.read().splitlines())

# string.ascii_lowercaseでa-zのアルファベット列を取れる
for c in string.ascii_lowercase:
  print("{} : {}".format(c, text.count(c)))