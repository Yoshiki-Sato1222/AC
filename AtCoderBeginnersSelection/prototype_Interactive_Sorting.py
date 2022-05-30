import sys


def check(num_1, num_2):
    print('?', num_1, num_2, flush=True)
    s = input()
    return s == '<' #num_1<num_2ならTrueを返す

def merge_sort(data):
    if len(data) == 1:
        return data

    mid = (len(data) // 2)#分割のための中央探索
    if len(data) % 2 == 0:
        left_list = merge_sort(data[:(mid)])#左半分の探索
        right_list = merge_sort(data[(mid):])#右半分の探索
    else:
        left_list = merge_sort(data[:(mid + 1)])#左半分の探索
        right_list = merge_sort(data[(mid + 1):])#右半分の探索

    return merge(left_list,right_list)


def merge(left_list,right_list):
    result = []
    i, j = 0, 0

    while (i < len(left_list)) and (j < len(right_list)):
        if check(left_list[i],right_list[j]):         #左<右のとき
            result.append(left_list[i])    #左側から1つ取り出して追加
            i += 1
        else:
            result.append(right_list[j])  #右側から1つ取り出して追加
            j += 1

    # 判定する必要がないため残りをまとめて追加
    if i < len(left_list):
        result.extend(left_list[i:])      #左側の残りを追加(判定終了)
    if j < len(right_list):
        result.extend(right_list[j:])    #右側の残りを追加(判定終了)

    return result

def merge_sort_2(data):
    #step2まで
    list1 = []
    save_data = data.pop()
    left_list = data[:2]
    right_list = data[2:]
    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)

    if check(left_list[0],right_list[0]):#left_list[0]<right_list[0])
        list1.append(left_list[0])
        list1.extend(right_list)
        save_data_3 = left_list[1]
    
    else:
        list1.append(right_list[0])
        list1.extend(left_list)
        save_data_3 = right_list[1]
    
    

    if check(list1[1],save_data): #c<e
        if check(list1[2],save_data):#d<e acde
            list1.append(save_data)
            if check(list1[2],save_data_3):#d<b
                if check(list1[3],save_data_3):#e<b
                    list1.append(save_data_3)
                else:
                    list1.insert(3,save_data_3)
            else:#d>b
                if check(list1[1],save_data_3):#c<b
                    list1.insert(2,save_data_3)
                else:
                    list1.insert(1,save_data_3)
    
    
        else:#list1[2]>save_data 
            list1.insert(2,save_data)#aced
            if check(list1[3],save_data_3):#d<b
                list1.append(save_data_3)
            else:#d>b
                if check(list1[2],save_data_3):#e<b
                    list1.insert(3,save_data_3)
                else:#e>b
                    if check(list1[1],save_data_3):#c<b
                        list1.insert(2,save_data_3)
                    else:#c>b
                        list1.insert(1,save_data_3)

    
    else:#c>e
        if check(list1[0],save_data): # a<e acd
            if check(save_data_3,list1[1]): #b<c
                if check(save_data_3,save_data):#b<e
                    list1.insert(1,save_data)
                    list1.insert(1,save_data_3)
                else:#b>e
                    list1.insert(1,save_data_3)
                    list1.insert(1,save_data)
            else: #c<b
                if check(save_data,list1[2]):#b<d
                    list1.insert(2,save_data)
                else:
                    list1.append(save_data_3)
        else:#e<a eacd
            list1.insert(0,save_data)
            if check(list1[2],save_data_3):#c<b
                if check(list1[3],save_data_3):#d<b
                    list1.append(save_data_3)
                else:
                    list1.insert(3,save_data_3)
            else:
                list1.insert(2,save_data_3)

    return list1
      

if __name__ == '__main__':

  [N, Q] = list(map(int, input().split()))
  c = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split()


  # ソート
  if N == 5:
    c_sorted = merge_sort_2(c[:N])

  else:
    c_sorted = merge_sort(c[:N])

  # ! ans
  print('!', ''.join(c_sorted), flush=True)
  sys.exit(0)