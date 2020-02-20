N = int(input())
A = list(map(int, input().split()))

def bubble_sort(array):
  l = len(array)
  swap = 0

  for i in range(0, l - 1):
    for j in range(l - 1, i, -1):
      if array[j] < array[j-1]:
        array[j], array[j-1] = array[j-1], array[j]
        swap += 1

  return swap

count = bubble_sort(A)
print(" ".join(map(str, A)))
print(count)