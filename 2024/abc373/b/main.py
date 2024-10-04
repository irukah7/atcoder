S = input()

ch = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# 前の文字とどのくらい離れているか計算する

ans = 0
tmp = S.index("A")
for c in ch:
  if S.index(c) >= tmp:
    tmp = abs(S.index(c)-tmp)
  else:
    tmp = abs(tmp-S.index(c))

  ans += tmp

  tmp = S.index(c)

print(ans)

