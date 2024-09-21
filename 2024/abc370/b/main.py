N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

tmp = 1
for i in range(1, N+1):
  if tmp >= i:
    tmp = A[tmp-1][i-1]
  else:
    tmp = A[i-1][tmp-1]

print(tmp)