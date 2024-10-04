N, Q = map(int, input().split())
S = list(input())

ans = 0

# 初期状態でABCがいくつあるか
for i in range(N-2):
  if S[i] == "A" and S[i + 1] == "B" and S[i + 2] == "C":
    ans += 1

for _ in range(Q):
  x, c = input().split()
  x = int(x)-1
  # 変更前にABCがいくつあるか
  for k in range(3):
    # 3パターンチェック
    idx = x - k
    if 0 <= idx and idx+2 < N:
      if S[idx] == 'A' and S[idx+1] == 'B' and S[idx+2] == 'C':
        # 3箇所それぞれチェックしてABCだったら-1
        ans -= 1

  S[x] = c

  # 変更後にABCがいくつあるか
  for k in range(3):
    # 3パターンチェック
    idx = x - k
    if 0 <= idx and idx+2 < N:
      if S[idx] == 'A' and S[idx+1] == 'B' and S[idx+2] == 'C':
        # 3箇所それぞれチェックしてABCだったら+1
        ans += 1

  print(ans)


