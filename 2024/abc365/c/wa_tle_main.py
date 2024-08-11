n, m = map(int, input().split())
L = list(map(int, input().split()))

# TLEコード
# n, m = 10**5 ,1
# L = [10**9] * n

maxM = int(m**0.5)
if m // (max(L)*n) >= 1:
  print('infinite')
else:
  for i in range(maxM, -1, -1):
    tmpM = m
    for j in range(n):
      tmpM -= min(i, L[j])

      if tmpM < 0:
        continue

    if tmpM >= 0:
      print(i)
      break