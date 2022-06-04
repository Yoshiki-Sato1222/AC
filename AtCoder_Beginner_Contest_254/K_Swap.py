#参考にしたサイト　https://atcoder.jp/contests/abc254/submissions/32210922
num_list = list(map(int,input().split()))

data_set = list(map(int,input().split()))
test_set = []
for i in range(num_list[1]):
  test_set.append([])
  
#ここでmodを用いて分けることが重要になっている　->同じリスト内なら自由に入れ替えて良いため...
for i in range(len(data_set)):
  test_set[i % num_list[1]].append(data_set[i])

#それぞれのリストをソート
for i in test_set:
  i.sort()


ans_list = []

#並べ直してみる
for i in range(num_list[0]):
  ans_list.append(test_set[i % num_list[1]][i // num_list[1]])
  
data_set = sorted(data_set)

#きちんとソートされているかの確認
if (data_set == ans_list):
  print("Yes")
else:
  print("No")

