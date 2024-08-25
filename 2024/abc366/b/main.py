N = int(input())
S = [input() for _ in range(N)]

# SiのMax文字列を取得する
m = max(map(len, S))
# 「Tiの末尾は＊ではない」を一旦無視して構成する
T = [['*'] * N for _ in range(m)]

for i in range(N):
  for j in range(len(S[i])):
    T[j][N-i-1] = S[i][j]

# 「Tiの末尾は＊ではない」ので削除する
for i in range(m):
  while T[i][-1] == '*':
    T[i].pop()

  print(''.join(T[i]))