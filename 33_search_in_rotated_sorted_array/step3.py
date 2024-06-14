class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left < right + 1:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            elif nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
        # 3'13

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            left_val = nums[left]
            mid = (left + right) // 2
            mid_val = nums[mid]
            right_val = nums[right]
            if target == left_val:
                return left
            elif target == mid_val:
                return mid
            elif target == right_val:
                return right
            elif left_val <= target <= mid_val:
                right = mid - 1
            elif left_val <= mid_val:
                left = mid + 1
            elif mid_val <= target <= right_val:
                left = mid + 1
            else:
                right = mid - 1
        return -1
""" 感想
読みやすいと思って X_val 変数を導入したが、むしろ手間だった。
変数を増やすというのはそれだけで把握しておくべきものを増やすことになる
慣れによって読みやすさのために導入した変数を冗長に感じるようになったのかもしれない。
"""
    # 4'21

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left < right + 1:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            elif nums[left] <= target <= nums[mid]:
                right = mid - 1
            elif nums[left] <= nums[mid]:
                left = mid + 1
            elif nums[mid] < target <= nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid - 1
        return -1
    # 2'36

""" 感想
なかなかスムーズに書けた。「頭に入っている」という感覚がある。
"""
