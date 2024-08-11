# n, m = map(int, input().split())
# L = list(map(int, input().split()))

# TLEコード
n, m = 10000 ,10000
L = [10000] * n

L.sort(reverse=True)
for i in range(m, 0, -1):
  tmpm = m
  for j in range(n):
    tmpm -= min(L[j], i)

  if tmpm >= max(L):
    print('infinite')
    break

  if tmpm >= 0:
    print(i)
    break


