N = int(input())
K = list(map(int, input().split()))

ans = 10**9

# 0~2**N-1まで試す
for s in range(1<<N):
  a, b = 0, 0
  for i in range(N):
    if s>>i & 1 == 0:
      a += K[i]
    else:
      b += K[i]

  now = max(a,b)
  ans = min(ans, now)

print(ans)
