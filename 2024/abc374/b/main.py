S = input()
T = input()

min_str = min(len(S), len(T))

ans = 0
flg = False
if S == T:
  print(0)
else:
  for i in range(min_str):
    if S[i] != T[i]:
      ans = i + 1
      flg = True
      break

  if not flg:
    ans = i + 2

  print(ans)