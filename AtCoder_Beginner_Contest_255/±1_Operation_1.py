import sys
num_1,A,D,N = map(int,input().split())

min_idx = 0 
start_num = 1 
end_num = N


if D < 0:
  A = A + D*(N - 1)
  D = -D
elif D == 0 or N == 1:
  print(abs(A - num_1))
  sys.exit()
  
max_1 = A + D*(N - 1)
  
for i in range(1000):
  if (start_num + end_num) % 2 == 0:#検討する要素が奇数個の場合
    if abs(A + D * (start_num - 1) - num_1) <= abs(A + D * (end_num - 1)- num_1):
      end_num = (start_num + end_num)//2
    elif abs(A + D * (start_num - 1) - num_1) > abs(A + D * (end_num - 1)- num_1):
      start_num = (start_num + end_num)//2
      
  else:#検討する要素が偶数個の場合
    if abs(A + D * (start_num - 1) - num_1) <= abs(A + D * (end_num - 1)- num_1):
      end_num = (start_num + end_num)//2
    elif abs(A + D * (start_num - 1) - num_1) > abs(A + D * (end_num - 1)- num_1):
      start_num = (start_num + end_num)//2 + 1
    
     
  if (end_num - start_num) == 1:
    min_1 = abs(min(abs(A + D * (start_num - 1) - num_1),abs(A + D * (end_num - 1) - num_1)))
    break
print(min_1)