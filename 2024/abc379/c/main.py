N, M = map(int, input().split())
X = list(map(int, input().split()))
A = list(map(int, input().split()))

masu = [0] * N
for i in range(M):
  masu[X[i]-1] = A[i]


print(masu)

# for i in range(N):
#   while :
#     if len(i+1) == 0:
