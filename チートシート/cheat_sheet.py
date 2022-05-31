import itertools

print("{} {}".format("これは","チートシートです"))

#複数の入力を受けた際にそれらをintでリストに保存する
num_list = list(map(int,input().split()))


#for文で複数回保存する(ただしpythonのfor文は若干速度が遅いので、競プロ等では注意すること...)
num_list_2 = []
for i in range(num_list[0]):
  num_list_2.append(list(map(int,input().split())))

print("今後内容を増やしていきます")