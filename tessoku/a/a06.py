n,q = map(int, input().split())
a = list(map(int, input().split()))

# あらかじめ累積和を保持しておく
S = [0] * (n+1)
for i in range(1, n+1):
  S[i] += S[i-1] + a[i-1]

for i in range(q):
  l, r = map(int, input().split())
  print(S[r] - S[l-1])

# TLE
# for i in range(q):
#   l,r = map(int, input().split())
#   ans = sum(a[l-1:r])
#   print(ans)