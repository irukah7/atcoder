A, B, C = map(int, input().split())

# 日を跨ぐ場合
if B > C:
  # C時より大きくてB時より小さかったら起きているので
  if C < A < B:
    print('Yes')
  else:
    print('No')
# 日を跨がない場合
else:
  # B時より大きくてC時より小さかったら寝ているので
  if not (B < A < C):
    print('Yes')
  else:
    print('No')
