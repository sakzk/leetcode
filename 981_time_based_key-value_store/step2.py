# bisect_left, bisect_right でコーナーケースの扱いに違いがでるため、両方で実装してみた。
class TimeMaOp:

    def __init__(self):
        self.key_to_values = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.key_to_values:
            self.key_to_values[key] = list()
        bisect.insort(self.key_to_values[key], (value, timestamp), key=lambda x: x[1])

    # bisect_right を使った get() の実装
    def get_right(self, key: str, timestamp: int) -> str:
        if key not in self.key_to_values:
            return ""
        target_index = (-1) + bisect_right(self.key_to_values[key], timestamp, key=lambda x: x[1])
        if target_index < 0:
            return ""
        return self.key_to_values[key][target_index][0]

    # bisect_left を使った get() の実装。
    def get_left(self, key: str, timestamp: int) -> str:
        insert_place = bisect_left(self.key_to_values[key], timestamp, key=lambda x: x[1])
        if insert_place == len(self.key_to_values[key]):
            return self.key_to_values[key][-1][0]
        if self.key_to_values[key][insert_place][1] == timestamp:
            return self.key_to_values[key][insert_place][0]
        if insert_place == 0:
            return ""
        return self.key_to_values[key][insert_place - 1][0]

# step1 からの変更点
"""
get_right:
- インデックスの調整
    - `insert_place - 1` に `target_index` という名前をつけた。`-1`によるインデックスの調整の意図が伝わりやすくなるかと思ったため。
    - bisect_right の項が長いので、 `(-1)` を式の最初に持ってきた。

get_left:
- bisect_left を使った実装はこれ以上きれいな記述は思いつかなかった。
    - return 文中のインデックスの指定が3パターンあり、条件文も3つあるのでのでいかにもミスしやすそう
    - 3つの条件文の並びは順序を崩してはいけない。
        - IndexError のケア → timestamp_prev == timestamp のケア → timestamp == 0 のケア→ これらがすべてに当てはまらないなら、bisect_left で見つけた一つ左の要素が対象要素のインデックス
"""
