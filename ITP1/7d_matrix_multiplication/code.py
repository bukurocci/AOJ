n,m,l = list(map(int, input().split()));

A = list();
B = list();
C = [[0 for _ in range(l)] for _ in range(n)]

for _ in range(n):
  row = list(map(int, input().split()));
  A.append(row);

for _ in range(m):
  row = list(map(int, input().split()));
  B.append(row);

#AxB
for i in range(n):
  for j in range(l):
    for k in range(m):
      C[i][j] += A[i][k] * B[k][j];

for row in C:
  print(" ".join(map(str, row)));

