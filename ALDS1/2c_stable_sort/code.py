N = int(input())
cards1 = input().split()
cards2 = cards1[:]

def bubble_sort(array):
  l = len(array)

  for i in range(0, l - 1):
    for j in range(l - 1, i, -1):
      a = int(array[j][1:])
      b = int(array[j-1][1:])
      if a < b:
        array[j], array[j-1] = array[j-1], array[j]

def selection_sort(array):
  l = len(array)
  
  for i in range(l):
    min_index = i

    for j in range(i, l):
      a = int(array[min_index][1:])
      b = int(array[j][1:])

      if(a > b):
        min_index = j

    if(min_index != i):
      array[i], array[min_index] = array[min_index], array[i]

bubble_sort(cards1)
print(" ".join(cards1))
print("Stable")
selection_sort(cards2)
print(" ".join(cards2))
print("Stable" if cards1 == cards2 else "Not stable")