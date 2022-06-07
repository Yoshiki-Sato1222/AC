import itertools

num_1,num_2 = map(int,input().split())
nums = list(map(int,input().split())) + [0,0]

#ans = []

'''for i in range(num_1 + 2):
  for j in range(i):
    for k in range(j):
      if nums[i] + nums[j] + nums[k] <= num_2:
        ans.append(nums[i] + nums[j] + nums[k])'''

ans_2 = []        
for i,j,k in itertools.combinations(nums,3):

  if i + j + k <= num_2:
    ans_2.append(i+j+k)
        
#ans = set(ans)
ans_2 = set(ans_2)

print(len(ans_2))      