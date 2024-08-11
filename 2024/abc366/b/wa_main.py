N = int(input())
S = [input() for _ in range(N)]

li = []
# 最大文字数M
m = 0

for s in reversed(S):
  tmp = []
  for c in s:
    tmp.append(c)
  m = max(m, len(tmp))
  li.append(tmp)


ans = []
n = 0

while n < m:
  tmp = []
  for i in range(len(li)):
    # liの長さが>=nなら
    if len(li[i])-1 >= n:
      tmp.append(li[i][n])
    else:
      tmp.append('*')

  ans.append(tmp)
  
  n += 1

# 末尾の＊を削除する
cnt = 1
for i in range(1, len(ans[-1])+1):
  if ans[-1][-i] == '*' or ans[-1][-i] == '':
    cnt += 1
  else:
    break

ans[-1] = list(ans[-1][:-cnt+1])

for a in ans:
  print(''.join(a))