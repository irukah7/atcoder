n, k = map(int, input().split())
A = list(map(int, input().split()))

ans = A[n-k:n]+A[0:n-k]
print(*ans)