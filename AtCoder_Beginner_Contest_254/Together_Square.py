#参考にしたサイト　https://qiita.com/u2dayo/items/e5f0a0f02c530f12b03b

from itertools import count

#自分が使ったもの(これだと時間的に無理...)
def calc_left(num):
  num_2 = 2
  while num > num_2:
    if num % (num_2 ** 2) == 0: 
      num //= (num_2 ** 2)
    else:
      num_2 +=1
  return num


#参考にしたサイトで用いられていた関数を参考にしたもの(pypy3なら通る)
def calc_remain(num):
    for num_2 in (i ** 2 for i in count(2)):
        if num_2 > num: 
            break
        while num % num_2 == 0: 
            num //= num_2 
      
    return num 

num_1 = int(input())
ans = 0

for i in range(1,num_1 + 1):
  left = calc_remain(i)
  for j in range(1,num_1 + 1):
    if left * (j ** 2) > num_1:
      break
    ans += 1
print(ans)