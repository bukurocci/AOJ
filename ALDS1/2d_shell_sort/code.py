n = int(input())
A = []
cnt = 0
m = 0
G = []

for _ in range(n):
    A.append(int(input()))

def insertion_sort(array, h):
  global cnt

  # 0番目は既にソート済み領域として考えて1から始める
  for i in range(h, len(array)):
    j = i - h

    # 現在のindexの値を保持しておく
    cur = array[i]

    # 配列を現在の1つ前のindexから0へ向かって cur より小さい値が見つかるまで遡る
    while(j >= 0 and array[j] > cur):
      # A[j] が curより大きい場合は A[j] の値を一つ後ろにシフトする
      array[j+h] = array[j]
      j -= h
      cnt += 1

    # jが配列の先頭にくるか、cur が A[j] より大きい場合
    # 値のシフトを完了する。この時 j+1 は cur が挿入されるべきindexになっている
    array[j+h] = cur

def shell_sort(array):
    global G, m
    # 最大間隔を決めるために配列長を取得する
    l = len(array)

    # 最大感覚は 9/l 以下にする
    h = 1
    # h(i+1) = 3 * h(i) + 1
    while h <= l and m <= 100 :
        G.append(h)
        h = 3 * h + 1
        m += 1

    G.reverse()

    for h in G:
        insertion_sort(array, h)


shell_sort(A)

print(m)
print(" ".join(map(str, G)))
print(cnt)
for value in A:
    print(value)

