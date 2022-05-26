#参考にしたページ   https://tysonblog-whitelabel.com/atcoder-beginners-selection_practice4

num = int(input())
list_1 = list(map(int, input().split()))
#答えとして出力する変数
num_1 = 0
#flagは割り切れなくなったらflag = 1となりbreakされる
flag = 0

while True:
  for i in range(num):
    if (list_1[i] % 2) != 0:
      flag = 1
  if flag == 1:
    break
  for i in range(num):
    list_1[i] = list_1[i]//2
  num_1 += 1
      
print(num_1)