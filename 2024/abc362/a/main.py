R,G,B = map(int, input().split())
C = input()

L = [R, G, B]
if C == 'Red':
  L.remove(R)
elif C == 'Green':
  L.remove(G)
elif C == 'Blue':
  L.remove(B)

print(min(L))
