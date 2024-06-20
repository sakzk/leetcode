from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.key_to_timestamped_value = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        bisect.insort(self.key_to_timestamped_value[key], (timestamp, value), key=lambda x: x[0])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_to_timestamped_value:
            return ""
        target_index = -1 + bisect_right(self.key_to_timestamped_value[key], timestamp, key=lambda x: x[0])
        if target_index < 0:
            return ""
        return self.key_to_timestamped_value[key][target_index][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

# 4'34 -> 3'48 -> 3'05

""" 備考
timestamped_value の語順に合わせて、 (timestamp, value) の順序でタプルを構築している。関数の定義も、`set(self, timestamp: int, valu: str):` とするのが自然かも。

target_index の取りうる値の範囲は `-1 <= target_index < len(self.key_to_timestamped_value[key])` なので、 `if target_index < 0` は、`if target_index == -1` でもよいかも。
"""
