N, T, P = map(int, input().split())
L = list(map(int, input().split()))

tmp = L.copy()
ll = 0
for t in tmp:
    if t >= T:
      ll += 1
    
if ll >= P:
  print(0)
  exit()

# T以上の長さの人を数える
def f(tmp, cnt):
  for t in tmp:
    if t >= T:
      cnt += 1

  if cnt > P:
    return cnt, True
  else:
    return cnt, False

i = 0
while True:
  tmp = list(map(lambda x: x+1, tmp))
  cnt = 0
  cnt, flg = f(tmp, cnt)
  if flg:
    break
  i += 1

print(i)