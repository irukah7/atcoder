N = int(input())
H = list(map(int, input().split()))

T = 0
for h in H:
  # 3回ワンセットで-5減算するのを繰り返しいるので何回繰り返しているか調べる
  mod = h//5
  # mod*3回数が加算される
  T += 3*mod
  # 要素からmod*5を減算する
  h -= 5*mod

  # あとは愚直に回す
  while h>0:
    T += 1
    if T%3 == 0:
      h -= 3
    else:
      h -= 1

print(T)