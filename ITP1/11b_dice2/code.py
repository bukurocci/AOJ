faces = list(map(int, input().split()))
n = int(input())

# 右回りに側面の展開図番号を保存する
patterns = [
  [1, 3, 4, 2],
  [5, 3, 0, 2],
  [1, 0, 4, 5],
  [1, 5, 4, 0],
  [0, 3, 5, 2],
  [1, 2, 4, 3]
]

for _ in range(n):
  top, front = list(map(int, input().split()))
  
  # 上面の値から面のindexを取得する
  ti = faces.index(top)

  # 前面の値から面のindexを取得する
  fi = faces.index(front)

  # indexから概要の側面パターンを取得したあとに
  # 前面の値から-1を引くと左側の値になる
  pattern = patterns[ti]
  ri = pattern[pattern.index(fi) - 1]

  print(faces[ri])


