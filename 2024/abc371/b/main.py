N, M = map(int, input().split())

# N戸の家の長男を初期値Falseにする
L = [False] * N

for i in range(M):
  A, B = map(str, input().split())
  A = int(A)

  # 家L[i]に長男が生まれているかチェック
  if B == 'M':
    if L[A-1]:
      # 既に生まれていたらNo
      print('No')
    else:
      # 生まれていなかったらTrueにして出力
      L[A-1] = True
      print('Yes')
  else:
    # 女の子は関係ないのでNoを出力
    print('No')