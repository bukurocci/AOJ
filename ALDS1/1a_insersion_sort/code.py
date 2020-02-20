N = int(input())
A = list(map(int, input().split()))

def insertion_sort(A, N):
  # 0番目は既にソート済み領域として考えて1から始める
  for i in range(1, N):
    # 一つ前のindexを取っておく
    j = i - 1

    # 現在のindexの値を保持しておく
    cur = A[i]

    # 配列を現在の1つ前のindexから0へ向かって cur より小さい値が見つかるまで遡る
    while(j >= 0 and A[j] > cur):
      # A[j] が curより大きい場合は A[j] の値を一つ後ろにシフトする
      A[j+1] = A[j]
      j -= 1

    # jが配列の先頭にくるか、cur が A[j] より大きい場合
    # 値のシフトを完了する。この時 j+1 は cur が挿入されるべきindexになっている
    A[j+1] = cur

    print(" ".join(map(str, A)))

print(" ".join(map(str, A)))
insertion_sort(A, N)