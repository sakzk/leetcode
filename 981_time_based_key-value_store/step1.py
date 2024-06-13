# 実装前ノート
"""
アルゴリズムの選択肢
- 選択にあたっては、set, get どちらの比重が高いか考える必要がある。要素がたくさんあって、get が多いなら、values はソートしてあるほうがよい。
- setでappend, get で線形探索
    - set O(1), get O(n)
- setでbisect.insort, get で binary_search
    - set O(n), get O(long_n)
    - insort は、挿入位置の探索に O(lon_n)、挿入に O(n) かかる

変数名の選択肢
- key_to_values, key_to_value_pairs, key_to_timestamped_values
    - 問題文から、key_to_values を使った。具体的な状況が与えらればもっとよいのを考える必要がある。
- `for v, timestamp_prev in self.key_to_values[key]:` の `v` はループ内なので1文字でよいかと判断した。
    - value にすると、ループの外側の value とかぶる。

データ構造
- key: string, value: List となる dictionary. import が必要だが defaultdict() でも書ける。
- set, get の他に、 update がある場合は tuple の他に list も選択肢に入る
    - 要素を削除して再度挿入するよりも、上書きして更新するほうが早いため
    - 今回は set, get のみ実装すればよいので tuple をいた。

注意が必要な仕様
- すべての timestamp_prev について、timestamp < time_stamp_prev だった場合は、該当なしとなる。
    - 今回は value を "" で初期化することで対応。
"""

# timestamp によるソートを行わない実装。leetcode の環境では TLE。
class TimeMap:

    def __init__(self):
        self.key_to_values = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.key_to_values:
            self.key_to_values[key] = list()
        self.key_to_values[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_to_values:
            return ""
        value = ""
        max_time_stamp_so_far = 0 #
        for v, timestamp_prev in self.key_to_values[key]:
            if timestamp_prev <= timestamp and max_time_stamp_so_far < timestamp_prev:
                value = v
                max_time_stamp_so_far = timestamp_prev
        return value

# 考察+実装20分、テストの脳内実行に6分。

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

# 改善点
"""
線形探索内部の条件判定の `if timestamp_prev <= timestamp and max_time_stamp_so_far < timestamp_prev:` は次のようにもかける
- `if max_time_stamp_so_far < timestamp_prev <= timestamp_prev:` 区間がわかりやすい

`max_time_stamp_so_far = 0` の初期値はコメントを付けたほうがいいい気がするが、よいのが思いつかない
- `max_time_stamp_so_far = 0 # Since there is no valid timestamp_prev, max_time_stamp_so_far remains zero.` これだと、挙動の説明をしているが、なぜ 0 が入っているかの理由にはなっていない。
- 値は、timestamp の取りうる値よりも小さければなんでもよい。0 のほかに -1 も選択肢。比較に用いるので None はだめ。
    - `max_time_stamp_so_far = 0 # It can be any value as long as it is smaller than the minimum possible value of timestamp` 長いけどこれはよさそう。
"""

# timestamp で values をソートする実装。
from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.key_to_values = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        bisect.insort(self.key_to_values[key], (timestamp, value), key=lambda x : x[0])
        return None

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_to_values:
            return ""
        insert_place = bisect.bisect_right(self.key_to_values[key], timestamp, key=lambda x : x[0])
        if insert_place == 0:
            return ""
        return self.key_to_values[key][insert_place - 1][1]

# 実装20分、脳内ラン9分

# 実装中ノート
"""
コーナーケースの扱い
- timestamp_prev == timestamp となるときの挙動
    - timestamp_prev <= timestamp となる最大の timestamp_prev を見つける問題なので、bisect_right を使うと簡単になることに気づいた。
    - テストケースを脳内実行して、insert_place == 0 のケアが必要なことに気づく。
"""

# 改善点
"""
set():
- 関数の型ヒントで None を返すと明示してあるので、 `return None` は書かない方に統一するのが良さそう。
- tuple の初期化
    - (a, b) でやる。tuple([a, b]) は冗長
"""
