import bisect

n, m = map(int, input().split())
A = list(map(int, input().split()))

if sum(A) <= m:
  print('infinite')
  exit(0)

A.sort()
lenA = len(A)
left = -1
right = m

while left + 1 < right:
  x = (left + right) // 2
  border = bisect.bisect_left(A, x)

  sumA = sum(min(x, a) for a in A)
  if sumA > m:
    right = x
  else:
    left = x

print(left)