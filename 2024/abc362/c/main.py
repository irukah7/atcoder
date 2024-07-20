N = int(input())
# L = [list(map(int, input().split())) for _ in range(N)]
# 安直にやってみる
patternL = []
for _ in range(N):
  L, R = map(int, input().split())
  patternL.append(list(range(L, R+1)))

# 無限に続くNの分だけfor文回してsum=0に探していたらTLEになる。。

print(patternL)