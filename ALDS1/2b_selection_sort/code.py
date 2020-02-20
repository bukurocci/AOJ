N = int(input())
A = list(map(int, input().split()))

def selection_sort(array):
  l = len(array)
  swap = 0
  
  for i in range(l):
    min_index = i

    for j in range(i, l):
      a = array[min_index]
      b = array[j]

      if(a > b):
        min_index = j

    if(min_index != i):
      array[i], array[min_index] = array[min_index], array[i]
      swap += 1

  return swap

count = selection_sort(A)
print(" ".join(map(str, A)))
print(count)
