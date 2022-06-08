from collections import defaultdict

num = int(input())
num_list = defaultdict(int)
idx = set()
for i in range(num):
  num_1 = list(map(int,input().split()))
  
  if num_1[0] == 1:
    x=num_1[1]
    num_list[x] += 1
    idx.add(x)
    
  elif num_1[0] == 2:
    x=num_1[1]
    num_list[x] = max(0,num_list[x] - num_1[2])    
    
  elif num_1[0] == 3 and len(idx) > 0:
    while num_list[min(idx)]==0:
      idx.remove(min(idx))
    while num_list[max(idx)]==0:
      idx.remove(max(idx))
    print(max(idx) - min(idx))  