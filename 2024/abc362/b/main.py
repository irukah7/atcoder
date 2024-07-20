xA,yA = map(int, input().split())
xB,yB = map(int, input().split())
xC,yC = map(int, input().split())

# 3:4:5が作れれば直角三角形になるので全通り試す
A = ((xB - xA) **2 + (yB - yA) **2) ** 0.5
B = ((xC - xB) **2 + (yC - yB) **2) ** 0.5
C = ((xA - xC) **2 + (yA - yC) **2) ** 0.5
ans = 'No'

# 何が間違ってるかわからない、WAになるデータが思い浮かばない

if round(A**2 + B**2) == round(C**2) or \
  round(B**2 + C**2) == round(A**2) or \
  round(C**2 + A**2) == round(B**2):
  ans = 'Yes'

print(ans)