data_list = list(map(int,input().split()))
food_num = list(map(int,input().split()))
dislike_num = list(map(int,input().split()))

max_1 = max(food_num)
max_index = [i+1 for i,v in  enumerate(food_num) if v == max_1 ]

    
if len(set(max_index) & set(dislike_num)) == 0:
  print("No")
else:
  print("Yes")