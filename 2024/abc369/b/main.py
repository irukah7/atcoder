N = int(input())

l = []
r = []
for n in range(N):
  A, S = input().split()

  if S == 'R':
    r.append(int(A))
  else:
    l.append(int(A))

sumL = 0
sumR = 0
for i in range(len(l)-1):
  sumL += abs(l[i]-l[i+1])
for i in range(len(r)-1):
  sumR += abs(r[i]-r[i+1])

print(sumL+sumR)