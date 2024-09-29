N, Q = map(int, input().split())
S = input()
S = [s for s in S]

for i in range(Q):
  x, c = input().split()
  x = int(x)
  S[x-1] = c

  print("".join(S).count('ABC'))
