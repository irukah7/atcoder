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

# 各行の末尾にある*を取り除く
for i in range(m):
  while ans[i][-1] == '*':
    ans[i].pop()

for a in ans:
  print(''.join(a))