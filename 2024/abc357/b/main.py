S = input()

mozi = sum(map(str.islower, S))
MOZI = sum(map(str.isupper, S))

if mozi > MOZI:
  print(S.lower())
else:
  print(S.upper())