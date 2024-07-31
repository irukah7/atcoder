n,k = map(int, input().split())

cnt = 0
for i in range(1, n+1):
  for j in range(1, n+1):
    if (k-i-j) <= n and (k-i-j) > 0:
      cnt += 1

print(cnt)