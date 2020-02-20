s = input() # 対象の文字列
n = int(input()) # 命令の数

# 命令の数だけ文字列を処理する
for _ in range(n):
  i = input().split()
  command = i[0]
  args = i[1:]
  a = int(args[0])
  b = int(args[1])

  if(command == "print"):
    print(s[a:b+1])
  elif(command == "reverse"):
    s = s[:a] + s[a:b+1][::-1] + s[b+1:]
  elif(command == "replace"):
    p = args[2]
    s = s[:a] + p + s[b+1:]