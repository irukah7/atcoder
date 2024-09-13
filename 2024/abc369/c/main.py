N = int(input())
A = list(map(int, input().split()))

cnt = 0
# (l, r)の範囲が2以下の時は必ず等差数列になる
for i in range(N):
  for j in range(i+3, N):
    # (l, r)の範囲で等差数列かどうか調べる
    x = A[i:j]
    half = j//2
    if j % 2 == 0:
      tmp = (x[half]+x[half])//2
    else:
      tmp = x[half]

    if sum(x)//j == tmp:
      cnt += 1

print(cnt)