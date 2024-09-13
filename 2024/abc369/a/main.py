A, B = map(int, input().split())
cnt = 0
for x in range(-220, 220):
  tmp = [x, A, B]
  tmp.sort()

  if tmp[2] - tmp[1] == tmp[1] - tmp[0]:
    cnt += 1

print(cnt)