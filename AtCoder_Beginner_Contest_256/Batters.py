num_1 = int(input())
num_list = []

num_list = (list(map(int,input().split())))
ans_list = [0 for i in range(num_1)]
for i in range(num_1):
  for j in range(i+1):
    ans_list[j] += num_list[i]

ans = 0
for i in range(num_1):
  if ans_list[i] > 3:
    ans += 1
    
print(ans)