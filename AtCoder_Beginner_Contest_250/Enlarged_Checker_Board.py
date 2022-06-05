list_1 = list(map(int,input().split()))

str_1 = []
str_2 = []

# .で始まるリストを作成する
for i in range(list_1[0]):
  for j in range(list_1[2]):
    if i % 2 == 0:
      str_1.append(".")
    else:
      str_1.append("#")

# #で始まるリストを作成する
for i in range(list_1[0]):
  for j in range(list_1[2]):
    if i % 2 == 0:
      str_2.append("#")
    else:
      str_2.append(".")

#リストを結合しておく     
str_1 = "".join(str_1)
str_2 = "".join(str_2)

#出力する
for i in range(list_1[0]):
  for j in range(list_1[1]):
    if i % 2 == 0:
      print(str_1)
    else:
      print(str_2)