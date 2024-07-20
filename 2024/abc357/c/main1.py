def f():
  grid = [['#'] * pow(3, N) for _ in range(pow(3, N))]
  for level in range(N+1):
    size = pow(3, level)
    cnt = pow(3, N) // size
    sub = size // 3
    for x in range(cnt):
      for y in range(cnt):
        """
          レベル = levelのカーペットのうち
          上からx番目、左からy番目の左上の座標(xi, yi)
        """
        xi = size * x
        yi = size * y
        """
          レベル = levelのカーペット9分割した時の、
          中央ブロックの左上の座標(si, sj)
        """
        si = xi + sub
        sj = yi + sub
        for i in range(si, si + sub):
          for j in range(sj, sj + sub):
            grid[i][j] = '.'
    
  return grid

N = int(input())
ans = f()
for row in ans:
  print(''.join(row))