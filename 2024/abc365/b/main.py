N = int(input())
A = list(map(int, input().split()))

dictA = {}
for i in range(N):
  dictA[A[i]] = i+1

A.sort(reverse=True)
num = dictA[A[1]]
print(num)
