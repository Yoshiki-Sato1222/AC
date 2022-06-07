# コード概要

## Six_Characters.py

A問題なので特に解説するまでもありませんが、6/(入力された文字数) 回繰り返し入力された文字列を繰り返すプログラムとなります

## At_Most_3.py

B問題ですが、若干工夫が必要となります。これは最初に入力された重みに0を二つ加えます。こうすることで重りを1つ、または2つだけ選ぶ場合を

```python

for i, j, k in itertools.combinations(nums, 3):

```
だけで考えることが可能となるからです。

## Poem_Online_Judge_TLE.py

自分で実装したもの(答え自体は正しいがTLEになります)。理由としておそらくオリジナルでないものの削除を行う際に探索数が多いため、時間が足りないのだと思います。

## Poem_Online_Judge.py

模範解答[模範解答](https://atcoder.jp/contests/abc251/editorial/3968)のコードになります
