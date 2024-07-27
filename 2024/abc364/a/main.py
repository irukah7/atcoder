N = int(input())

tmp = ""
for i in range(N-1):
  S = input()
  if tmp == S and S == 'sweet':
    print('No')
    exit(0)
  tmp = S

print('Yes')
