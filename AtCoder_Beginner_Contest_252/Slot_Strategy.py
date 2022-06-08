import numpy as np

slot_num = int(input())

slot_ans = [[] for i in range(slot_num)]
slot = []

for i in range(slot_num):
  slot.append(input())
  

for i in range(10):
  for j in range(slot_num):
    num = str(i)
    slot_ans[j].append(slot[j].index(num) + 1)
    
min_num = 11
min_idx = -1

slot_ans = np.array(slot_ans).T.tolist()
  
time = []
for i in range(len(slot_ans)):
  if slot_ans[i] == list(set(slot_ans[i])):
    time.append(max(slot_ans[i]) - 1)
  else:
    equal_num = 0
    ans_num = 0
    for j in range(1,11):
      if equal_num <= slot_ans[i].count(j):
        ans_num = j
        equal_num = slot_ans[i].count(j)
    
    time.append(ans_num - 1 + (equal_num - 1) * 10)
    
print(min(time))