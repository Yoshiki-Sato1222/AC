num_1 = int(input())

list_1 = []

for i in range(1,num_1+1):
  test_list = []
  for j in range(i):
    if (j == 0 or j == i-1):
      test_list.append(1)
    else:
      test_list.append(list_1[i - 2][j - 1] + list_1[i - 2][j])
      
  list_1.append(test_list)
    
for i in range(len(list_1)):
  print(*list_1[i])