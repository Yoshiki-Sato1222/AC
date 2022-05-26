num = list(map(int,input().split()))
ans = 0
for i in range(1,num[0]+1):
  num_3 = 0
  num_2 = i
  for n in range(0,5):
    num_3 += num_2 // (10 ** (4 - n))
    num_2 -= (10 ** (4 - n)) * (num_2 // (10 ** (4 - n)))
  if num[1] <= num_3 <= num[2]:
    ans += i
print(ans)