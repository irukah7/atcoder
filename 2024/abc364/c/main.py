N,X,Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse=True)
B.sort(reverse=True)

sumA = 0
sumB = 0
cnt = 0
for i in range(N):
  if sumA > X or sumB > Y:
    break
  sumA += A[i]
  sumB += B[i]
  cnt += 1

print(cnt)