import sys

turn = int(input())
lines = [line.strip().lower() for line in sys.stdin]

points = [0, 0]

for pair in lines:
  cards = pair.split()
  
  if(cards[0] == cards[1]):
    points[0] += 1
    points[1] += 1

  elif(cards[0] > cards[1]):
    points[0] += 3
  
  elif(cards[0] < cards[1]):
    points[1] += 3

print(" ".join(map(str, points)))
