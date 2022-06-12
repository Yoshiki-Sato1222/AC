import math

num_list = list(map(int,input().split()))

have_list = list(map(int,input().split()))

data_list = []

for i in range(num_list[0]):
  data_list.append(list(map(int,input().split())))
  
light_list = []

for i in reversed(have_list):
  light_list.append(data_list.pop(i - 1))

max_list = [[] for i in range(len(data_list))]
for i in range(len(data_list)):
  for j in range(len(light_list)):
    max_list[i].append(math.sqrt((data_list[i][0] - light_list[j][0]) ** 2 + (data_list[i][1] - light_list[j][1]) ** 2))
    
min_list = []
for i in range(len(max_list)):
  min_list.append(min(max_list[i]))
  
print(max(min_list))