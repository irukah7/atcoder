N = int(input())
L, R = [0] * N, [0] * N

for i in range(N):
  L[i], R[i] = map(int, input().split())

if sum(L) > 0 and sum(R) < 0:
  print('No')
  exit()

X = L.copy()
sumX = sum(X)
for i in range(N):
  d = min(R[i]-L[i], -sumX)
  