ab, ac, bc = map(str, input().split())

# 組み合わせは６パターン
# abc, acb, bac, bca, cab, cba

# abc, cba
if (ab == '<' and ac == '<' and bc == '<') or (ab == '>' and ac == '>' and bc == '>'):
  print('B')
# acb, bca
elif (ab == '<' and ac == '<' and bc == '>') or (ab == '>' and ac == '>' and bc == '<'):
  print('C')
# bac, cab
else:
  print('A')

