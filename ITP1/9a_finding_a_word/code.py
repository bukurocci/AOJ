import sys

word = sys.stdin.readline().strip().lower()
lines = []
count = 0

for line in sys.stdin:
  if(line == "END_OF_TEXT"): break
  words = line.strip().lower().split(' ')
  count += words.count(word)

print(count)