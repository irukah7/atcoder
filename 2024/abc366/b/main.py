N = int(input())
S = [input() for _ in range(N)]

# 最大値Mを取得する
m = 0
for s in S:
  m = max(m, len(s))

revS = list(reversed(S))
ans = []
for i in range(m):
  tmp = []
  for j in range(len(S)):
    if len(revS[j])-1 >= i:
      tmp.append(revS[j][i])
    else:
      tmp.append('*')
  ans.append(tmp)

# 最後の行だけ回す
cnt = 0
for i in range(len(ans[m-1])-1, -1, -1):
  if ans[m-1][i-1] == '*':
    cnt -= 1
  else:
    break

ans[m-1] =list(ans[m-1][:cnt-1])

for a in ans:
  print(''.join(a))