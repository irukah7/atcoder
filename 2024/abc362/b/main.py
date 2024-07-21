xA,yA = map(int, input().split())
xB,yB = map(int, input().split())
xC,yC = map(int, input().split())

ans = 'No'
# 2点間の距離を求める
AB = (xB - xA) **2 + (yB - yA) **2
BC = (xC - xB) **2 + (yC - yB) **2
CA = (xA - xC) **2 + (yA - yC) **2

# 3平方の定理より直角かどうか調べる
if AB + BC == CA or \
  BC + CA == AB or \
  CA + AB == BC:
  ans = 'Yes'

print(ans)