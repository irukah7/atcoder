N = int(input())

# levelNのgridを作成する
grid = [['#'] * pow(3, N) for _ in range(pow(3, N))]



for row in grid:
  print(''.join(row))