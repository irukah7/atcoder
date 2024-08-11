N,T,A = map(int, input().split())

# 残り投票数
p = N - (T+A)
if T > A:
  if T <= (p+A):
    print('No')
  else:
    print("Yes")
else:
  if A <= (p+T):
    print("No")
  else:
    print('Yes')