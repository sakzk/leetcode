# bisectライブラリーを使って書く

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_min(nums: List[int]) -> int:
            return bisect_left(nums, True, key=lambda x: x <= nums[-1])
        # ソート済の2つの区間に分割するため、最小値の leftmost を探索
        min_index = find_min(nums)
        # target の探索：両区間に target が含まれている場合、左区間をの結果を使う
        if nums[0] <= target <= nums[min_index - 1]:
            insert_place =  bisect_left(nums, target, 0, min_index - 1)
        else:
            insert_place =  bisect_left(nums, target, min_index, len(nums))
        return insert_place if insert_place < len(nums) and nums[insert_place] == target else -1


    # target の探索の表現のバリエーション
        # その1：右区間にセットして、左区間の結果で上書きする
            # 区間の要素が一つのとき、[low, hi) = [0, 1) なので探索区間が空にならない。
            # 右にある区間を先に探索するので、数直線の並びからみて、不自然に感じる。
            # 右の区間に存在せず、左の区間に存在するとき、rightmost = len(nums) が発見された場所のインデックスで上書きされる。
        # 発見されないときは insert_place = len(nums) 据え置きで return -1  に入るので仕様をみたす。
        insert_place = bisect_left(nums, target, min_index, len(nums))
        if nums[0] <= target <= nums[min_index - 1]:
            insert_place =  bisect_left(nums, target, 0, min_index - 1)

        # その2：左区間の探索結果をセットして、右区間の結果で上書きする
            # 区間の要素が一つのとき、[low, hi) = [0, min_index=0) となって探索区間が空になる。
            # そのため 明示的にmin_index + 1 して右半開区間にする必要がある。
            # 左の区間を先に探索するのは数直線の並びから見て自然だが、右区間に存在ししない場合、
            # len(nums) で 左区間から得たinsert_placeを上書きしてしまう。
        # 見つかっているものを見つかっていないことにしてしまうので仕様を *** 満たさない。***
            # 上書きしないためには、存在することを確認してから探索を開始しなければならないが、今からやることを前提として使っているので、繰り返しになる。
        insert_place = bisect_left(nums, target, 0, min_index + 1)
        if nums[min_index] <= target:
            insert_place = bisect_left(nums, target, min_index, len(nums))

"""
発想：最小値を境界にして、ソート済の2つの区間に分割できる (minがnums[0]の場合は一つ)

実装上の注意点：
- bisectの引数、返り値について
    - 引数：bisectにスライスを与えると、スライス内のインデックスが帰ってくる。区間の限定はスライスではなく オプション引数 hi, lo の指定でおこなう。
    - 返り値：挿入位置を返すので、「見つからない」は `nums[bisect返り値]  == target` でチェックする必要がある
- insort()がappend()とおなじになるとき、IndexError を起こさないために `insert_place < len(nums)` でチェックする

最小値の探索: bisect_left で探すとインデックスがそのままつかえる。
- ソート済区間の分割のためには、最小値の leftmost で区切るのが自然。
- [5, 6, 1, 1, 2, 3, 4] -> left:[5, 6]/[1, 1, 2, 3, 4], right:[5, 6, 1, 1]/[2, 3, 4]
- [4, 5, 6, 1, 1, 3, 4] -> left:[4, 5, 6]/[1, 1, 3, 4], right:[4, 5, 6, 1, 1]/[3, 4]

target の探索：返り値を、target 全部見つける、にした場合、どのように変更するか
- 入力配列に含まれるものをすべての target 見つけたいなら、左右の区間どちらとも探索する必要がある。
    - 区間内の要素の個数は、インデックスと個数の関係に注意して、'bisect_right() - bisect_left()'で求められる。
        - 存在しない場合は、差が 0 になる。非存在を特殊ケースとして扱わなくていい
        - 区間ごとに low をインクリメンタルしながら binsect_left を呼ぶのは煩雑になりそう。
"""
