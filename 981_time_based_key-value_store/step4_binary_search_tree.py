# timestamp をキーにした二分探索木で、timestamped_values を実装する。(時間計算量の最悪状態に近いため leetcode 環境ではTLE)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Constraints:
# 1. 1 <= key.length, value.length <= 100
# 2. key and value consist of lowercase English letters and digits.
# 3. 1 <= timestamp <= 107
# 4. All the timestamps timestamp of set are strictly increasing.
# 5. At most 2 * 105 calls will be made to set and get.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class Node:
    def __init__(self, key: int=None, value: str=None, left=None, right=None): # 型のtypo
        self.key = key
        self.value = value
        self.left = left
        self.right = right
    
    def __str__(self): # デバッグ用
        return f"{self.key}, {self.value}, (l: {self.left}), (r:{self.right})"

class TimeMap:
    def __init__(self):
        self.key_to_timestamped_value = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.key_to_timestamped_value:
            self.key_to_timestamped_value[key] = Node(timestamp, value)
            return
        root = self.key_to_timestamped_value[key]
        while root:
            if root.key < timestamp and not root.right:
                root.right = Node(timestamp, value)
                return
            elif root.key >= timestamp and not root.left: # key が重複する Node は 左のサブツリーに追加する。
                root.left = Node(timestamp, value)
                return
            if root.key < timestamp:
                root = root.right
            elif root.key >= timestamp:
                root = root.left
        raise Exception("Something wrong with set() method: there may be duplicate timestamps.")
    
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_to_timestamped_value:
            return ""
        value = ""
        root = self.key_to_timestamped_value[key]
        while root:
            if root.key <= timestamp:
                value = root.value
                root = root.right
            else:
                root = root.left
        return value

"""
設計の選択：binary search tree を tree として実装するか、array で実装するか
- array による binary search tree の実装：parent のインデックスを `i` として、左の子を インデックス `2i + 1`, 右の子を インデックス `2i + 2` の要素とすればいい。
array で実装する場合の計算コストの見積もり：
今回は、配列に 10^14 要素分の領域が必要になる。(1 <= timestamp <= 10^7 であり、かつ、key となる timestamp の値は増加するいっぽうなので 「要素数 = 深さ」となる。空間計算量として最悪の状況で配列はスカスカ)
  - python の int 型のオブジェクトの大きさは、64ビット環境で 28byte~ : https://stackoverflow.com/questions/10365624/sys-getsizeofint-returns-an-unreasonably-large-value
      - `sys.getsizeof(Node())` は 48 byte なので実際に必要するメモリは int 型を格納するときの2倍ぐらい必要になる。
  - 実消費メモリの概算
    - 概算 (int型だけを入れる想定)：28byte * 10^14 = 2.8B * (1000)^5 ≒ 3B * (2^10)^5
      - (2^32bit = 4GiB の数倍を遥かに超えているので手元のマシンのメモリには収まらない大きさ。)
    - 実際に配列を作ってみる：`[0 for _ in range(10**9)]` で、`8806512088 byte` ≒ 9 GB
        - これに 10^5 をかけて、9GB * 10^5 = 9 * 10^9 * 10^5 = 9 * 10^14。概算の1/3倍ぐらい
        - 900TB
          - 参考 `>>> sys.getsizeof([0 for _ in range(10**10)]) # 82547110552 byte`
    - いずれにしてもメモリに収まりきらない
  - 実時間
    - 配列の初期化`cProfile.run('[0 for _ in range(10**8)]')` で約3秒かかり線形増加するので初期化だけで 3 * 10^6 秒かかる。
以上より、今回は array で binary search tree を構築するのは厳しそう。

計算量の見積もり：
- set(), get()
  - いずれの操作も木がバランスされているとき O(log_n)、木が偏っているとき O(n)
  - 今回は問題の制約より、キーが単調増加するので右の木が伸び続ける。追加位置を見つけるのも、対象をサーチするのも線形リストを辿っているのとおなじになる。

二分探索の delete (未実装)：
削除する対象を見つけたら、左のサブツリーの最大値 (or 右のサブツリーの最小値) で上書きして、上書きに使った葉のノードを削除する。
参照：https://www.geeksforgeeks.org/deletion-in-binary-search-tree/

時刻の制約と binary search tree の設計について：
timestamp に重複がなく、値が単調増加するというのは時刻のデータであれば妥当な仮定思われる。他方、時間の粒度によっては同じタイムスタンプがついてもおかしくない。
今回の問題は左のサブtree に入れると探索範囲がきれいに二分できるのでそうした。(timestamp_prev <= timestamp)

時刻関連のリンク集：
Pythonの時刻を扱うモジュール：https://docs.python.org/ja/3/library/time.html
Unix Time 1970年1月1日からの経過時間を固定長2進数で表現する：https://en.wikipedia.org/wiki/Unix_time
2038年には32ビットがオーバーフローする：https://en.wikipedia.org/wiki/Year_2038_problem
"""  
