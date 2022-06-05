list_1 = list(map(int,input().split()))

set_list = list(map(int,input().split()))

num = 0
#横幅が1の場合に処理を行わない
if list_1[0] > 1:
    if set_list[0] == 1 or set_list[0] == list_1[0]:
        num += 1
  
    else:
        num+= 2
  
#縦の長さがが1の場合に処理を行わない
if list_1[1] > 1:
    if set_list[1] == 1 or set_list[1] == list_1[1]:
        num += 1
  
    else:
        num += 2
  
#(1,1)ならば処理を行わないため0を返すことが保証される
print(num)