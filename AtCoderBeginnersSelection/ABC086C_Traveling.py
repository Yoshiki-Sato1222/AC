num_1 = int(input())
start = [0,0,0]
list_1 = []
for i in range(num_1):
  list_1.append(list(map(int,input().split())))

list_1 = [start] + list_1
for i in range(1,len(list_1)):
  time_dis = list_1[i][0] - list_1[i - 1][0]
  dist = abs(list_1[i][1] - list_1[i - 1][1]) + abs(list_1[i][2] - list_1[i - 1][2])
  if dist - time_dis > 0 or (time_dis - dist) % 2 != 0:
    print("No")
    break
  else:
    if i == len(list_1) - 1:
      print("Yes")