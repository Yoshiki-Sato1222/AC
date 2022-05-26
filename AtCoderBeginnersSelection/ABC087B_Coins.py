num = []
ans = 0
for i in range(4):
  num.append(int(input()))
for i in range(0,num[0]+1):
  for j in range(0,num[1]+1):
    for k in range(0,num[2]+1):
      if (500 * i + 100 * j + 50 * k) == num[3]:
        ans += 1
print(ans)