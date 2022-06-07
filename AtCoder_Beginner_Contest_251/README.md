# コード概要

## Six_Characters.py

A問題なので特に解説するまでもありませんが、6/(入力された文字数) 回繰り返し入力された文字列を繰り返すプログラムとなります

## Six_Characters.py

## At_Most_3.py

B問題ですが、若干工夫が必要となります。これは最初に入力された重みに0を二つ加えます。こうすることで重りを1つ、または2つだけ選ぶ場合を

```python

for i, j, k in itertools.combinations(nums, 3):

```
だけで考えることが可能となるからです。
