while True:
  word = input()

  if(word == "-"):
    break

  num_shuffle = int(input())

  for _ in range(num_shuffle):
    p = int(input())
    word = word[p:] + word[:p]
  
  print(word)