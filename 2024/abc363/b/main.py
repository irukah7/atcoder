N, T, P = map(int, input().split())
L = list(map(int, input().split()))

for i in range(100):
  tmpL = L.copy()
  cnt = 0
  for j in range(N):
    tmpL[j] += i
    if tmpL[j] >= T:
      cnt += 1

  if cnt >= P:
    print(i)
    break