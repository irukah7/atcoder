Q = int(input())

# 要素に対して減算加算をするための箱を作っておく　
T = [0] * (10**6)
ans = 0
for i in range(Q):
  t, *x = list(map(int, input().split()))
  if t == 1:
    x[0] -= 1
    # Tの要素に+1加算
    T[x[0]] += 1
    # 要素が1、つまりボールが既に入っていない時種類数は増える
    if T[x[0]] == 1:
      ans += 1
  elif t == 2:
    x[0] -= 1
    # Tの要素に-1減算
    T[x[0]] -= 1
    # 要素が0、つまりボールが袋に入っていない時種類数は減る
    if T[x[0]] == 0:
      ans -= 1
  else:
    print(ans)
