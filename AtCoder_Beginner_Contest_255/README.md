# コード概要

## You_should_output_ARC_though_this_is_ABC.py

最初の入力で指定された二つの値に対応するリスト番号の値を返すコードになっています

## Light_It_Up.py

この問題は全ての点を照らす際に、明かりの強さの最小値を求める問題であった。
一見すると難しく見えるが、要するに各点を照らす際にそれぞれの点を照らすのに必要な明かりの最小値を求めそれらの最大値を求めれば答えが導かれる問題であった。
(入力例1であれば(0,0)は明かりの強さ1で照らされ、(2,0)は$\sqrt{5}$で照らされるためmin(1,$\sqrt{5}$)より$\sqrt{5}$が答えとなっていた)

## ±1_Operation_1.py

この問題は初項から順に比べていくと計算時間が最悪O(N)となりTLEとなる。
そこでこのコードではまず例外処理として

```python
elif D == 0 or N == 1:
  print(abs(A - num_1))
  sys.exit()
```
で交差か項数が0の場合の処理を行なう。

これらに該当しない場合には、初項と末項でどちらの値が求める答えに近いのか比較をしていく

```python
for i in range(1000):
  if (start_num + end_num) % 2 == 0:#検討する要素が奇数個の場合
    if abs(A + D * (start_num - 1) - num_1) <= abs(A + D * (end_num - 1)- num_1):
      end_num = (start_num + end_num)//2
    elif abs(A + D * (start_num - 1) - num_1) > abs(A + D * (end_num - 1)- num_1):
      start_num = (start_num + end_num)//2
      
  else:#検討する要素が偶数個の場合
    if abs(A + D * (start_num - 1) - num_1) <= abs(A + D * (end_num - 1)- num_1):
      end_num = (start_num + end_num)//2
    elif abs(A + D * (start_num - 1) - num_1) > abs(A + D * (end_num - 1)- num_1):
      start_num = (start_num + end_num)//2 + 1
    
     
  if (end_num - start_num) == 1:
    min_1 = abs(min(abs(A + D * (start_num - 1) - num_1),abs(A + D * (end_num - 1) - num_1)))
    break
```

これにより計算量は項数Nが$2^n \leq N \leq 2^{(n + 1)}$の時、O($\log N$)に抑えられるためTLEせずに済む。

コードの内容は、初項の方が答えに近い場合には末項をend_numから(start_num + end_num)//2に変更し、末項の値の方が答えに近い場合には、項数が奇数であれば初項をstart_num = (start_num + end_num)//2、そうでなければstart_num = (start_num + end_num)//2 + 1としている。
そして最終的に項数が二つになったところで、適切な値を取り出してbreakしてfor文を抜けている。
