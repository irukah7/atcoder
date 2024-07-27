H, W = map(int, input().split())
Si, Sj = map(int, input().split())
C = [input() for _ in range(H)]
X = input()

Si -= 1
Sj -= 1

for x in X:
  if x == 'L' and Sj-1 >= 0:
    if C[Si][Sj-1] != '#':
      Sj -= 1
  elif x == 'R' and Sj+1 <= W-1:
    if C[Si][Sj+1] != '#':
      Sj += 1
  elif x == 'U' and Si-1 >= 0:
    if C[Si-1][Sj] != '#':
      Si -= 1
  elif x == 'D' and Si+1 <=H-1:
    if C[Si+1][Sj] != '#':
      Si += 1
    
print(Si+1, Sj+1)
