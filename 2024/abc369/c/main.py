import itertools

N = int(input())
A = list(map(int, input().split()))

# Aの等差数列Bを考える
B = [0] * (N-1)
for i in range(len(A)-1):
  B[i] += A[i+1] - A[i]

# (1,1), (2,2)など等差数列1の組み合わせはN個あるので初期値N
ans = N
# 同じ差が連続しているところは等差数列であるといえるのでカウントを取る
count = 1
for i in range(N-1):
  if i == (N-2):
    # Bの最後の要素まで来たらカウントした値の合計を取る（連続した値が1の場合は1になる）
    ans += (count * (count + 1)) // 2
  elif B[i+1] == B[i]:
    # 連続している場合カウントを加算する
    count += 1
  else:
    # 連続していない場合そこまでのカウントした値の合計を取る
    ans += (count * (count + 1)) // 2
    # countを1に戻す
    count = 1

print(ans)