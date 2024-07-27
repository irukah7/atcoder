import more_itertools

N, K = map(int, input().split())
S = input()

ans = 0
for t in more_itertools.distinct_permutations(S):
  ok = True
  for i in range(N-K+1):
    u = t[i:i+K]
    if u == u[::-1]: ok = False

  if ok: ans += 1
print(ans)