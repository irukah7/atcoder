d = int(input())
n = int(input())

S = [0] * (d+1)
# 出席者数の前日比を記録する
# 例）2~10日目に出席した場合、2日目の前日比を+1, 10日目の前日比を-1する
for i in range(n):
  l, r = map(int, input().split())
  S[l] += 1
  S[r+1] -= 1

# 累積和を計算する
B = [0] * (d+1)
for i in range(1, d+1):
  B[i] = B[i-1] + S[i]

for b in B:
  print(b)

# O(d*N)=(10^5 * 10^5) でTLE
# S = [0] * (d+1)
# for _ in range(n):
#   l, r = map(int, input().split())
#   for i in range(l, r+1):
#     S[i] += 1

# print(S)
