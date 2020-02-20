while True:
  #これで文字列を1文字ずつの配列に変換できる
  s = list(input())

  if(s[0] == '0'):
    break

  print(sum(int(n) for n in s));
  #print(sum(list(map(int, s))))
