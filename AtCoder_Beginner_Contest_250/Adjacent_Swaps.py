list_1 = list(map(int,input().split()))

data = list(range(1+list_1[0]))#配列
index_num = list(range(list_1[0] + 1))#i番目の数字がどこにあるかを記録しておくリスト

for i in range(list_1[1]):
  x = int(input())#入れ替える数
  fi = index_num[x]#xのインデックス
  se = fi + 1 if fi != list_1[0] else fi - 1#交換先のインデックス
  y = data[se]#交換先の数
  
  data[fi], data[se] = data[se], data[fi]
  
  #交換しておく(xのインデックスとyのインデックス)
  index_num[x] = se
  index_num[y] = fi

#0は不要なので削除する
data.pop(0)

print(*data)