def length(a, d, g, j):
  s = max(a, g)
  t = min(d, j)
  return max(0, t - s)

a,b,c,d,e,f = map(int, input().split())
g,h,i,j,k,l = map(int, input().split())

"""
x, y, z軸でそれぞれ共通部分を持つか調べる
"""
Lx = length(a, d, g, j)
Ly = length(b, e, h, k)
Lz = length(c, f, i, l)

"""
直方体の体積を調べる
"""
V = Lx * Ly * Lz
if V > 0:
  print('Yes')
else:
  print('No')