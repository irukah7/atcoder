from collections import deque

N = int(input())

# Nを2進数に直して10桁で出力する
ans = deque([])
while N >= 2:
  mod = N % 2
  N //= 2

  ans.appendleft(str(mod))

# 最後は必ず1になる
ans.appendleft('1')

# 10桁になるまで0埋めする
while len(ans) != 10:
  ans.appendleft(0)


print(''.join(map(str, ans)))