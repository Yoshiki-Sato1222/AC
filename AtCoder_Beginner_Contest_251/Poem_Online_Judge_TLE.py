import copy

num = int(input())
data_list = []

for i in range(num):
  data_list.append(input().split())

data_list_2 = copy.copy(data_list)
  
for i in range(num):
  if i > len(data_list_2):
    break
  for j in reversed(range(i+1,len(data_list_2))):
    if data_list_2[i][0] == data_list_2[j][0]:
      data_list_2.pop(j)

top = -1
ans_num = 0

for i in range(len(data_list_2)):
  if top < int(data_list_2[i][1]):
    top = int(data_list_2[i][1])
    ans_num = i

print(data_list.index(data_list_2[ans_num]) + 1)