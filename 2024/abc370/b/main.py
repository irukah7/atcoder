N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
  if 1 >= i:
    tmp = A[0][i]
  else:
    tmp = A[i][0]

