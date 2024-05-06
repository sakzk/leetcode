"""
コメントを受けて、previousの初期値にnums[0]つかって実装。

3通りの制御で書いた。今回は分岐の両枝とも重さが同じぐらいなので、if-elseで分岐して、ループの終わりで共通の処理を行う実装が自然に感じる。
lengthの更新とlongest_lengthの更新の順序が違うことも強調される。

nums[1] 以降のすべての要素を取り出すにはnums[1::]をつかう。
[a:]よりも[a::]のほうが step を書き忘れているのではないことが伝わるような気がする。

ifの内部で num と書くべきところを nums と書いてもエラーは出ない。
変数名に num のかわりに value を採用するとこのミスが防げる。
"""

# if-elseで分岐
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        sorted_nums = sorted(set(nums))
        longest_length = 1
        length = 1
        previous = sorted_nums[0]
        for num in sorted_nums[1::]:
            if num == previous + 1:
                length += 1
                longest_length = max(length, longest_length)
            else:
                longest_length = max(length, longest_length)
                length = 1
            previous = num
        return longest_length 

# 連続条件成立でcontinue
# num のかわりに value をつかう
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
          
        sorted_nums = sorted(set(nums))
        longest_length = 1
        length = 1
        previous = sorted_nums[0]
        for value in sorted_nums[1::]:
            if value == previous + 1:
                length += 1
                longest_length = max(length, longest_length)
                previous = value
                continue
            longest_length = max(length, longest_length)
            length = 1
            previous = value
        return longest_length 

# 連続条件不成立でcontinue
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        sorted_nums = sorted(set(nums))
        longest_length = 1
        length = 1
        previous = sorted_nums[0]
        for num in sorted_nums[1::]:
            if num != previous + 1:
                longest_length = max(length, longest_length)
                length = 1
                previous = num
                continue
            length += 1
            longest_length = max(length, longest_length)
            previous = num
        return longest_length 
