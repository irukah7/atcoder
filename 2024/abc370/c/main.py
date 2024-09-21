S = list(input())
T = list(input())

X = []
# 先頭から見る
for i in range(len(S)):
  if S[i] > T[i]:
    S[i] = T[i]
    X.append(S[:])

# 後ろから見る
for i in reversed(range(len(S))):
  if S[i] < T[i]:
    S[i] = T[i]
    X.append(S[:])

print(len(X))
for x in X:
  print(''.join(x))