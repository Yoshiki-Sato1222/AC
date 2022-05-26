num = list(map(int,input().split()))
flag = 0
for i in range(0,num[0] + 1):
  for j in range(0, num[0]+ 1 - i):
    if ((10000 * i) + (5000 * j) + (1000 * (num[0] - i - j))) == num[1]:
      print("{} {} {}".format(i, j, num[0] - i - j))
      flag = 1
    if flag == 1:
      break
  if flag == 1:
    break
if flag == 0:
  print("{} {} {}".format(-1, -1, -1))