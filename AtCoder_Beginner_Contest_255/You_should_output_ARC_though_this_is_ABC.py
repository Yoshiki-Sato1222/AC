num_1,num_2 = map(int,input().split())
num_list = []
for i in range(2):
  num_list.append(list(map(int,input().split())))
  
print(num_list[num_1 - 1][num_2 -1])