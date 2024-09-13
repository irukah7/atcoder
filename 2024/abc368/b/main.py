N = int(input())
A = list(map(int, input().split()))

cnt = 0
# 正の要素が1つ以下になるまで繰り返す
while True:
  # 降順に並べ替える
  A.sort(reverse=True)

  if A[1] == 0:
    break
  
  # 1ずつ減らす
  A[0] -= 1
  A[1] -= 1
  cnt += 1

print(cnt)