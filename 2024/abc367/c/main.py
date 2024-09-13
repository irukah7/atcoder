import itertools

N, K = map(int, input().split())
R = list(map(int, input().split()))

# 全探索
li = list(itertools.product(*[range(1, r+1) for r in R]))

print(li)

for l in li:
  if sum(l) % K ==0:
    print(*l)

