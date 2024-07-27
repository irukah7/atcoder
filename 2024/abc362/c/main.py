N = int(input())
L, R = [], []

for i in range(N):
  _L, _R = map(int,input().split())
  L.append(_L)
  R.append(_R)

# 最小値はsum(L), 最大値はsum(R)となるのでL<=0<=Rとなるか確認する
if not (sum(L) <= 0 and 0 <= sum(R)):
  print('No')
  exit()

X = sum(L)
# 最小値から0にするために必要なcnt数
cnt = -X

for i in range(N):
  # 最大値R[i]よりも小さかったらL[i]にcnt全て足す
  if R[i] >= L[i]+cnt:
    L[i] = L[i]+cnt
    break
  # 最大値R[i]よりも大きかったら最大値R[i]までcntを足して、残りのcntを次の要素に回す
  else:
    cnt -= (R[i]-L[i])
    L[i] = L[i]+(R[i]-L[i])

if sum(L) == 0:
  print('Yes')
  print(*L)