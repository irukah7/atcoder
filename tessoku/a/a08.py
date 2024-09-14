H, W = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(H)]
Q = int(input())
A = [None] * Q
B = [None] * Q
C = [None] * Q
D = [None] * Q
for i in range(Q):
  A[i],B[i],C[i],D[i] = map(int, input().split())

# 横方向に累積和を作る
li = [[0]*(W+1) for _ in range(H+1)]
for i in range(1, H+1):
  for j in range(1, W+1):
    li[i][j] = X[i-1][j-1] + li[i][j-1]

# それを縦方向に累積和を作る
for j in range(1, W+1):
  for i in range(1, H+1):
    li[i][j] = li[i-1][j] + li[i][j]

# 矩形の4点の値を見て合計を算出する
# 右下+左上-右上-左下
for i in range(Q):
  print(li[C[i]][D[i]] + li[A[i]-1][B[i]-1] - li[A[i]-1][D[i]] - li[C[i]][B[i]-1])