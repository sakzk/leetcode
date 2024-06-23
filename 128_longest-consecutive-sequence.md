# 128 longest-consecutive-sequence
問題へのリンク: [https://leetcode.com/problems/longest-consecutive-sequence/](https://leetcode.com/problems/longest-consecutive-sequence/)

題意の理解：ソートされていない整数値の配列が与えられる。配列に含まれる整数値が連続する最長の長さを求めよ。重複は含まない。

入出力例：
- [] -> 0
- [1, 2, 3] -> 3
- [3, 2, 2, 1] -> 3

# step1
## アプローチ1: 配列中の最小値から最大値まで数え上げながら、連続する限りカウントアップ、途切れたらリセット。

計算量:
- Time O(k) kは最大値と最小値の差の絶対値。min, maxの探索でnumを2回トラバースする。 入力の制約 -10^9 <= num[i] <= 10^9 より、最悪で10^18回ループを回すことになる。案の定TLE。
- Space O(1)

実装上の注意：
- `range(lower_limit, upper_limit)`は [lower_limit, upper_limit)になってしまう。
  - 解決：+2にすることで、途切れを発生させて、for内のelse-if内の max_sequence_length の再代入処理に入るようにした。

```py
# アプローチ5分、実装6分、デバッグ開始して12分後にタイムアウトの原因に気づく
def longestConsecutive(self, nums: List[int]) -> int:
    if not nums:
        return 0

    lower_limit = min(nums)
    upper_limit = max(nums)
    nums = set(nums)

    max_sequence_length = 0
    sequence_length = 0
    for i in range(lower_limit, upper_limit + 2):
        if i in nums:
            sequence_length += 1
            continue
        else:
            if max_sequence_length < sequence_length:
                max_sequence_length = sequence_length
            sequence_length = 0
    return max_sequence_length
```

改善点：
- max_sequence_lengthは0で初期化しているので、numsがからであるときに0を返す処理はわざわざ書かなくてよい
- sequence_lengthをtypoしがち
- `upper_limit + 2`の処理に頭を使うので解消したい

## アプローチ2：ソートしてから、配列のはじめから終わりまで、連続する限りカウンアップ、途切れたらリセット。最大長は毎ループ更新。

計算量：
- Time O(nlogn) ソートにO(nlogn), その後のトラバースにO(n)かかる。
- Space O(n)？
    - https://github.com/python/cpython/blob/main/Doc/howto/sorting.rst
        - sorted()は新しいオブジェクトを作る。list.sort()はインプレース
        - アルゴリズムは Timsortと呼ばれている。 https://en.wikipedia.org/wiki/Timsort merge sortの改良版。
        - sorted()は安定ソート
        - sorted()の比較は `<` なので、昇順にソートされる。引数でreverse=Trueを指定すると降順になる。
    - https://github.com/python/cpython/blob/f6b5d3bdc83f8daca05e8b379190587a236585ef/Objects/listobject.c#L2850
        - list.sort()の本体。300行程度の定義のうち、keyの処理に半分ぐらいの行数を費やしている。
        - runを見つけてから merge しているのは名前から予想がつくが、データ構造、状態がたくさん出てきて理解しきれていない。
    - ソートの実装と計算量の見積もりについて https://discord.com/channels/1084280443945353267/1200089668901937312/1202464646913589328

実装上の注意：
- 重複でカウントアップが途切れることを防ぐため、ソートするまえにset()に入れる。
- max_lengthの更新をループ毎に行うようにした。
  - numsの末尾に入力を途切れさせるような数値を番兵としてappendして、ループの終わりにelse内での更新を発生させることで、リスト最後の連続塊に対しても「途切れたときだけ更新する」を実現できる。しかし、そこそこややこしい上に、forループ入る前に空配列が来たら0をreturnする処理付け足す必要があるため選ばなかった。

```py
def longestConsecutive(self, nums: List[int]) -> int:
    sorted_nums = sorted(set(nums))

    max_length = 0
    length = 0
    previous = -10^9 - 2 # -10^9 - 2 and the successor are not included as an element.
    for num in sorted_nums:
        if num == previous + 1:
            length += 1
        else:
            length = 1
        previous = num
        max_length = max(length, max_length)

    return max_length
```
ミス：(step2で修正)
- 実装では、累乗に `^` を使うのは間違い。`**`を使う。
  - 今回はすべてのジャッジに通ってしまったので書き直すまで気づかなかった。危ない。
  - ビット演算には `&, |, ^, ~, >>, <<` がある。https://docs.python.org/3/reference/expressions.html#binary-bitwise-operations


# step2

## ソートする解法の表現を改善
修正点：
- アプローチ2の累乗計算を、算術演算上正しい`**`に修正した。

改善点：
- previousの初期値を入力の上限値+1 にした。 下限-2よりもわかりやすいと感じる。Noneはintと足し算できないので初期値として使えない。

```py
# 2周目：問題を読んでから通るまで12分
def longestConsecutive(self, nums: List[int]) -> int:
    sorted_nums = sorted(set(nums))
    max_length = 0
    length = 0
    previous = 10**9 + 1
    for num in sorted_nums:
        if num == previous + 1:
            length += 1
        else:
            length = 1
        previous = num
        max_length = max(length, max_length)
    return max_length
```

## step2 別アプローチの検討: 連続の先頭要素に対してのみ、lengthを増やしながら`num + length`と一致する後続がどこまで存在するか調べていく。

実装上の注意:
- whileループに入る前に連続の起点であることを検査している。すべての要素が最大2回だけチェックされるので O(n) に抑えられている。(これがないと、連続の2番め以降の要素はなんどもwhileの条件文にひっかかる)
    - 継続条件なしだと、O(n^2)になる。 (最悪で 1/2*n^2 例：[1, 2, 3, 4, 5])

```py
# 実装のみ 2'45 (何度か練習したあと)
def longestConsecutive(self, nums: List[int]) -> int:
    nums = set(nums)
    max_length = 0
    length = 0
    for num in nums:
        if num - 1 in  nums:
            continue
        while num + length in nums:
            length += 1
        max_length = max(max_length, length)
        length = 1
    return max_length
```
# step3:

```py
# 実装2'17
import math

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        max_length = 0
        length = 0
        previous = math.nan
        for num in sorted_nums:
            if num == previous:
                continue
            if num == previous + 1:
                length += 1
            else:
                length = 1
            if max_length < length:
                max_length = length
            previous = num
        return max_length
```

実装バリエーション：
- set()を使うかわりに、制御側で num == previous となる num が来たらスキップする
- max()を使わずに再代入をif文で書き下す

ミスの原因：
- sorted_numsではなくnumsでイテレータにしてループを回していていた
- previousのtypo
- set()するのを忘れていた
- numと書くべきところをnumsと書いていた
    - リストとintを比較したらシンタックスエラーにして欲しい気持ちになる
- 2'13 (sort), 2'33 (sort), 1'55(sort), 1'55 (set), 2'17(sort)

# 追加：問題の制約をゆるめると回答をどのように変化させる必要があるか？

## -10^9 <= nums[i] <= 10^9 がないとき、previousを何で初期化すべきか？
- 浮動小数点数の比較は注意が必要
    - テキトーに絶対値が大きい値にしておくと、比較対象のnumが近い数だった場合に`if num[0] == previoius + 1` の真偽が変わるかもしれない。(丸め誤差)
    - float、算術演算の落とし穴
        - https://discord.com/channels/1084280443945353267/1084283898617417748/1199292102161481778
        - https://discord.com/channels/1084280443945353267/1200089668901937312/1200674405995524136
- nan自身を含むどんな数と比較してもFalseを返す数として定義されている math.nan を使うとよさそう。 https://docs.python.org/3/library/math.html#math.nan

## 重複する要素を連続とみなすとしたらどう変更するか？

ソートして数え上げのアプローチ：numとpreviousとの比較に少し追加するだけ

```py
def longestConsecutive(self, nums: List[int]) -> int:
    sorted_nums = sorted(nums)
    max_length = 0
    length = 0
    previous = 10**9 + 1
    for num in sorted_nums:
        if num == previous or num == previous + 1:
            length += 1
        else:
            length = 1
        previous = num
        max_length = max(length, max_length)
    return max_length
```

setを探索するアプローチ: あらかじめ文字の出現回数を数えておいて、出現回数の分だけlengthをインクリメントする
```py
def count_chars(nums: List[int]): # -> Dictionary
    char_count_map = dict()
    for num in nums:
        if num not in char_count_map:
            char_count_map[num] = 0
        char_count_map[num] += 1
    return char_count_map

def longestConsecutive(self, nums: List[int]) -> int:
    char_count_map = count_chars(nums)
    nums = set(nums)
    longest_length = 0

    for num in nums:
        if num - 1 not in nums:
            length = 1
            while num + length in nums:
                length += char_count_map[num+length]
            longest_length = max(longest_length, length)
    return longest_length
```

表現のバリエーション:
- `if num - 1 in nums: break; ~~` だと、「その数が後続ならスキップ、そうでないなら起点なので~~する」。
- `if num - 1 not in nums: ~~` だと、「その数が起点なら~~をする」。notを使うが、これぐらいなら `is_start(num)`と関数化するまでもないと感じる。

好み：
- `while num + length in nums:` でループを回す方が、目の縦幅の動きが少ないので好み。ソートする解法よりも整理されているように感じる。
