N = int(input())
S = input()

if N >= 2:
  cnt = 0 
  for i in range(N-2):
    if S[i+1] == '.':
      if S[i] == '#' and S[i+2] == '#':
        cnt += 1
  print(cnt)
else:
  print(0)