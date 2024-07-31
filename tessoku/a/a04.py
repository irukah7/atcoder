n = int(input())

tmp = ''
if n > 1:
  while True:
    s = n % 2
    n //= 2
    tmp = str(s) + tmp
    if n == 2:
      tmp = '10' + tmp
      break
    elif n == 1:
      tmp = '1' + tmp
      break
else:
  tmp = '1'

print(tmp.zfill(10))