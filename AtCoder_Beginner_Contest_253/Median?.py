num_1,num_2,num_3 = map(int,input().split())

if (num_1 - num_2) * (num_3 - num_2) <= 0:
  print("Yes")
  
else:
  print("No")