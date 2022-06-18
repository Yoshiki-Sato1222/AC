def nums(n):
  list_1 = []
  for i in range(1,n-1):
    for j in range(1,n-1):
      for k in range(1,n-1):
        if i + j + k == n:
          list_1.append([i,j,k])
  return list_1

num_list = list(map(int,input().split()))

list_1 = nums(num_list[0])
list_2 = nums(num_list[1])
list_3 = nums(num_list[2])
ans = 0
for i in range(len(list_1)):
  for j in range(len(list_2)):
    for k in range(len(list_3)):
      if list_1[i][0] + list_2[j][0] + list_3[k][0] == num_list[3] and list_1[i][1] + list_2[j][1] + list_3[k][1] == num_list[4] and list_1[i][2] + list_2[j][2] + list_3[k][2] == num_list[5]:
        ans += 1
        

print(ans)