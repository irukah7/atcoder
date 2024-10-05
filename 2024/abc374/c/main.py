N = int(input())
K = list(map(int, input().split()))

# sortして左と右端同士を足していく、残りを足したやつも保持する
K.sort()

if N == 2:
  print(max(K[0], K[1]))
else:
  max_division = 0
  min_num = 10 ** 8
  left = 1
  right = N - 1
  
  # 右端だけがBに所属する
  A = sum(K[:right])
  B = sum(K[right:])
  max_division = max(A, B)
  min_num = min(max_division, min_num)

  # 左端だけがAに所属する
  A = sum(K[:left])
  B = sum(K[left:])
  max_division = max(A, B)
  min_num = min(max_division, min_num)
  
  while left - 1 < right:
    A = sum(K[:left]) + sum(K[right:])
    B = sum(K[left:right])
    
    # 人数が多い方の部署を保持しておく
    max_division = max(A, B)
    min_num = min(max_division, min_num)

    if (sum(K[:left+1]) + sum(K[right:])) < (sum(K[:left]) + sum(K[right-1:])):
      left += 1
    else:
      right -= 1

  print(min_num)


