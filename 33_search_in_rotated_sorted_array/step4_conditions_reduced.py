# 条件式をできるだけ減らしたバージョン。区間と条件式を組み替える練習としておこなった。
from typing import List

def search_correctly_only_when_no_duplicates(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left < right + 1:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[left] <= target < nums[mid] or\
                (nums[mid] < nums[right] and (target < nums[mid] or nums[right] < target)):
                # if target may be in the left-interval or
                # target cannot be in the right-interval.
            right = mid - 1
        else:
            left = mid + 1
    return -1

def search_correctly_even_when_duplicates_exist(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left < right + 1:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[left] <= target < nums[mid] or\
                (nums[mid] <= nums[right] and (target < nums[mid] or nums[right] < target)):
                    # example: [3, 1, 1] -> [3]. right moves 2 to 0.
                # if target may be in the left-interval or
                # target cannot be in the right-interval.
            right = mid - 1
        else:
            left = mid + 1
    return -1

# 制御構造を変形したバリエーション。
# 二分探索は if-elif-else で書くのに慣れているので、ややイレギュラーに感じる。
# 可読性向上が増すというわけでもないと感じる。

def search(self, nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left < right + 1:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= target < nums[mid] or\
                (nums[mid] <= nums[right] and (target < nums[mid] or nums[right] < target)):
                # コメントは省略
            right = mid - 1
            continue
        left = mid + 1
    return -1

"""
やったこと：
- right, left の更新が別々のパスで実行されていたのを一つにまとめた。
- はじめは、`num[left] <= target < num[mid] or not(num[mid] < target <= num[right])` 単純に連結していたがこれは間違い
    - not の中身の条件が強すぎて、else に通すべきものを上で拾っていた。
        - not つきの、`not(num[mid] < target <= num[right])` は右区間がソートされていない場合も含んでしまう。
        - ソートされていない場合は区間内にあるかもしれないので、「ソート済の右区間内に無い」に条件を絞る
    - ここらへんの変形はかなり注意深く見ないと間違えてしまう。
        - typo、思い違い、形式操作の間違いなど。いろいろハマり要素があるので、詰まったらいじるより書き直すほうがよいかも。
        - 意味的に考えているのか、形式的な操作をしているのか区別しながらやるとハマりにくい。
感想：
- 分岐を減らすと一度に気にするべきことが減るので考えやすい。
- or, and が増えてくると条件式の連結ミスでしやすくなる。
    - 今回は if-elif-else で条件式をまとめてみたが、 or を分割して if-elif-elif-else ぐらいにするのが良さそう。
"""

# デバッグのやり方
"""
正しく動くことが確認できている元の実装をコピペして、巻戻せるようにしておく。
思い通りに行かない最小ケースを作る。
よーく見る。部分ごとに確かめていく。
    - バグさがしも二分探索
    - 上から下に見ていく
"""

# 以下、テスト
# no duplicates, found
print(search_correct_even_when_duplicates_exist([1], 1))
print(search_correct_even_when_duplicates_exist([3, 1, 2], 3))
print(search_correct_even_when_duplicates_exist([3, 1, 2], 1))
print(search_correct_even_when_duplicates_exist([3, 1, 2], 2))
print()

# no duplicates, not found
print(search_correct_even_when_duplicates_exist([1], 0))
print(search_correct_even_when_duplicates_exist([3, 1, 2], -1))
print(search_correct_even_when_duplicates_exist([3, 1, 2], 4))
print()

# duplicates exist, found
print(search_correct_even_when_duplicates_exist([3, 1, 3], 3))
print(search_correct_even_when_duplicates_exist([1, 1, 3], 1)) # 左区間が nums[left] <= nums[mid]
print(search_correct_even_when_duplicates_exist([3, 1, 1], 3)) # 右区間で nums[mid] <= nums[right]
print(search_correct_even_when_duplicates_exist([3, 3, 3], 3))
print()

# duplicates exist, not found
print(search_correct_even_when_duplicates_exist([3, 3, 2], -1))
print(search_correct_even_when_duplicates_exist([3, 3, 3], 4))
