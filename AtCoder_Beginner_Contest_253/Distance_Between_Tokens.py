num_1,num_2 = map(int,input().split())
map_1 = []
ans_list = []
flag = 0

for i in range(num_1):
  map_1.append(input())

for i in range(num_1):
  for j in range(num_2):
    if map_1[i][j] == "o":
      ans_list.append([i,j])
      flag += 1
  if flag == 2:
    break

ans = abs(ans_list[0][0] - ans_list[1][0]) + abs(ans_list[0][1] - ans_list[1][1])
print(ans)