num_1 = int(input())
num_2 = list(map(int,input().split()))
num_2 = sorted(num_2,reverse = True)
Alice = 0
Bob = 0
for i in range(len(num_2)):
  if i % 2 == 0:
    Alice += num_2[i]
  else:
    Bob += num_2[i]
print(Alice - Bob)