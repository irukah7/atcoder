#%%
# A
a, b = map(int, input().split())

print(format(b/a, '.3f'))
# %%
# B
h, w = map(int, input().split())
c = [list(map(str, input().split())) for _ in range(h)]

for j in range(w):
    count = 0
    for i in range(h):
        if c[i][0][j] == '#':
            count += 1
    print(count, end=' ')
# %%
# C
import sys
sys.setrecursionlimit(10**6)
N = int(input())
A = list(map(int, input().split()))

ans = [0]*(2*N+1)
for i,a in enumerate(A):
    ans[2*i+1] = ans[a-1]+1
    ans[2*i+2] = ans[a-1]+1
# %%
