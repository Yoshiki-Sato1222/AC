num = int(input())
num_1 = []
for i in range(num):
  num_1.append(int(input()))
num_2 = set(num_1)
print(len(num_2))