# step2 バージョン1
"""
- step1 からの余分な条件式を削除。変数も削除
- これだけでかなりスッキリする
    - 答えだけ見ると簡単そうだが、 nums[] でどこかで typo しそう。
    - かけたものの中では簡潔さではこれが一番。
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[left] <= target < nums[mid]:
                right = mid - 1
            elif nums[left] <= nums[mid]:
                left = mid + 1
            elif nums[mid] <= target <= nums[right]:
                left = mid + 1
            elif nums[mid] <= nums[right]:
                right = mid - 1
        return -1

# step2 バージョン2
"""
- 手作業の感じで。「こっちにあるので、そっちにはないのでこっちに来てください」&「こっちにはないので、そっちにあるのでそっちに行きます」
- else をつかうと、区間を「こっち、そっち」レベルでラフに扱っている感じがする。
- 条件式の漏れは else-else が処理している。
    - 書くのは楽になるが、読むのが楽になる感じはしない。脳内テストを走らせるときは else の意味を脳内で再構築するので難しさは減らない。
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            mid_val = nums[mid]
            left_val = nums[left]
            right_val = nums[right]
            if mid_val == target:
                return mid
            elif left_val <= mid_val:
                if left_val <= target < mid_val:
                    right = mid - 1
                else: # target might be in right-half interval.
                    left = mid + 1
            else: # right-half interval is sorted
                if mid_val <= target <= right_val:
                    left = mid + 1
                else: # target might be in left-half interval.
                    right = mid - 1
        return -1

# step2 バージョン3
"""
- コメントを丁寧にしてみたバージョン。かなり親切に感じる
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # nums[left] and nums[right] are used to check the rotation of sub-intervals.
        # left and right are inclusive pointers of the closed interval.
        # This avoids an IndexError when accessing nums[left] and nums[right].
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            mid_val = nums[mid]
            left_val = nums[left]
            right_val = nums[right]
            if left_val == target:
                return left
            elif mid_val == target:
                return mid
            elif right_val == target:
                return right
            elif left_val <= target <= mid_val:
                right = mid - 1
            elif left_val <= mid_val:
                left = mid + 1
            elif mid_val < target < right_val:
                left = mid + 1
            elif mid_val < right_val:
                right = mid - 1
        return -1

# 再帰でも書く
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def search_helper(left, right):
            if left > right:
                return -1
            mid = (left + right) // 2
            left_val = nums[left]
            mid_val = nums[mid]
            right_val = nums[right]
            if left_val == target:
                return left
            elif mid_val == target:
                return mid
            elif right_val == target:
                return right
            elif left_val < target < mid_val:
                return search_helper(left, mid - 1)
            elif left_val <= mid_val:
                return search_helper(mid + 1, right)
            elif mid_val < target < right_val:
                return search_helper(mid + 1, right)
            elif mid_val <= right_val:
                return search_helper(left, mid - 1)
        return search_helper(0, len(nums) - 1)

# バグ原因 & 対策
"""
- whileループでは継続条件なので left <= right だが、再帰の base case では停止するので反転。
    - 無限ループの原因としてロジックの考慮漏れを疑い始めてしまい気づくのに時間がかかった
    - 対策：デバッグの方針として、勘もいいけど、調べるのが簡単なところから固めていく感じのほうがいい。
        - 明らかに停止する文を書いておく `if true: return "stop"`
- return の書き忘れ
    - 返り値を返すパスに入っていない関数は None を返す。
    - 値が入っているはずのところに None が入っていたら疑う。
        - 返り値があると思い込んだ文も、バグの原因だと気づきにくい。
    - 対策：呼び出す前に return を書く
        - 本体を書き始める前に、底に `return "something went wrong"` みたいなものを書いておくと明示的に気づける
- どちらもテンプレートをつかうようにすれば防げる問題だが、それだと練習としては楽をし過ぎという気がするので保留。
"""

