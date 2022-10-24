#%%
# A
N = int(input())
ans = 1
for i in range(1, N+1):
    ans *= i
print(ans)
#%%
# A
X, K = map(int, input().split())

for i in range(K):
    if (X//(10**i))%10 >= 5:
        X += 10**(i+1)
    X -= X%(10**(i+1))
print(X)

# %%
