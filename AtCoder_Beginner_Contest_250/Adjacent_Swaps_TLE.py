list_1 = list(map(int,input().split()))

swap_case = []

for i in range(list_1[1]):
  swap_case.append(int(input()))

swap_data = []
for i in range(list_1[0]):
  swap_data.append(i + 1)


for i in range(list_1[1]):
  num_1 = swap_data.index(swap_case[i])
  if num_1 == list_1[0] - 1:
    swap_data[num_1 - 1],swap_data[num_1] = swap_data[num_1],swap_data[num_1 - 1]
  else:
    swap_data[num_1],swap_data[num_1 + 1] = swap_data[num_1 + 1],swap_data[num_1]
    
print(*swap_data)