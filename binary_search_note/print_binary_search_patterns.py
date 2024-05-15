##############################################################
# 目的: 二分探索アルゴリズムのインデックス更新の経過を観察する
##############################################################
# 実装にあたって注意すること
#   インデックスエラーを出さないこと(midが 0~len(nums)-1に収まること)
#   区間の端が漏れないこと
#   無限ループにならないこと (left, mid, right が固定されないこと)
##############################################################
# left, right の初期値に応じて4通りの実装がある
# inはinclusive, exはexclusiveを略している
##############################################################

from typing import List

OUTER_OF_WHILE_LOOP = 10000 # print_indexesをwhile ループの外で利用するためだけの意味のない変数

def print_binary_search_in_left_in_right(nums: int, target: int) -> int:
    left = 0
    right = len(nums) - 1
    print_indexes(nums, left, mid=OUTER_OF_WHILE_LOOP, right=right)
    while left < right + 1:
        mid = (left + right) // 2
        print_indexes(nums, left, mid, right)
        if nums[mid] == target:
            print("found!")
            return mid
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    print("not_found!")
    return -1

def print_binary_search_in_left_ex_right(nums: int, target: int) -> int:
    left = 0
    right = len(nums)
    print_indexes(nums, left, mid=OUTER_OF_WHILE_LOOP, right=right)
    while left < right:
        mid = (left + right) // 2
        print_indexes(nums, left, mid, right)
        if nums[mid] == target:
            print("found!")
            return mid
        elif target < nums[mid]:
            right = mid
        else:
            left = mid + 1
    print("not_found!")
    return -1

def print_binary_search_ex_left_in_right(nums: int, target: int) -> int:
    # 要素数が1のとき、mid = -1 になるが、pythonでは list[-1] は配列末尾の要素を指すためOK
    # 要素数が0のとき、left=-1, right=0 でループに入り、mid=-1で空配列に対するインデックスエラーを出すのでエラーハンドリングする
    if not nums:
        return -1
    left = -1
    right = len(nums)
    print_indexes(nums, left, mid=OUTER_OF_WHILE_LOOP, right=right)
    while left < right:
        mid = (left + right) // 2
        print_indexes(nums, left, mid, right)
        if nums[mid] == target:
            print("found!")
            return mid
        elif target < nums[mid]:
            right = mid
        else:
            left = mid + 1
    print("not_found!")
    return -1

def print_binary_search_ex_left_ex_right(nums: int, target: int) -> int:
    left = -1
    right = len(nums)
    print_indexes(nums, left, mid=OUTER_OF_WHILE_LOOP, right=right)
    while left < right - 1:
        mid = (left + right) // 2
        print_indexes(nums, left, mid, right)
        if nums[mid] == target:
            print("found!")
            return mid
        elif target < nums[mid]:
            right = mid
        else:
            left = mid
    print("not_found!")
    return -1

# 探索対象のリストを対応するインデックスとともに出力する
def print_list_to_search(nums: int, digit: int=3) -> None:
    """
        0  2  4  6  8 10  12 14 16 18 20 22 24
     -1 0  1  2  3  4  5  6  7  8  9  10 11 12
    のように、要素とインデックスを出力する。
    -1 と len(nums)+1 も出力して、left = -1, right = len(nums) での初期化に対応する
    """
    # print item in order
    item_line = []
    item_line.append(" " * digit)
    for i in range(len(nums)):
        item_line.append("{:<{digit}}".format(nums[i], digit=digit))
    print("".join(item_line))

    # pirnt indexes in order
    index_line = []
    for i in range(-1, len(nums)+1):
        index_line.append("{:<{digit}}".format(i, digit=digit))
    print("".join(index_line))
    return None

# left, mid, right のインデックスを出力する
def print_indexes(nums: List[int], left: int, mid: int, right: int) -> None:
    """
    -1 0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 # この行は print_list_to_searchにより出力される
    l______________________________________m______________________________________r__
    のように、3桁を1つのインデックスに対応させて、インデックスに対応する位置に l, m, r を出力する
    この例は、left = -1, right = len(nums) で初期化したもの。

    空なら `___`, left, middle, rightに順に l__, m__, r__ が出力される
    -1 と len(nums)+1 の桁も出力して、left = -1, right = len(nums) での初期化に対応する
    """
    size = len(nums) + 2
    line = []
    left += 1
    mid += 1
    right += 1
    cell_prefix = ""
    for i in range(size):
        if i == left and i == mid and i == right:
            cell = "lmr"
        elif i == left and i == mid:
            cell = "lm_"
        elif i == mid and i == right:
            cell = "mr_"
        elif i == left and i == right: # it doesn't happen.
            cell = "lr_"
        elif i == left:
            cell = "l__"
        elif i == mid:
            cell = "m__"
        elif i == right:
            cell = "r__"
        elif i == 0 or size:
            cell = "___"
        else:
            cell += "   "
        line.append(cell_prefix + cell)
    print("".join(line))
    return None

# 4つの実装ごとの実行経過を出力する
def run_binary_search_patterns(lst: List[int], target: int) -> None:
    print("in_left_in_right", "target", target)
    print_list_to_search(lst)
    print_binary_search_in_left_in_right(lst, target)
    print()

    print("in_left_ex_right", "target:", target)
    print_list_to_search(lst)
    print_binary_search_in_left_ex_right(lst, target)
    print()

    print("ex_left_in_right", "target", target)
    print_list_to_search(lst)
    print_binary_search_ex_left_in_right(lst, target)
    print()

    print("ex_left_ex_right", "target", target)
    print_list_to_search(lst)
    print_binary_search_ex_left_ex_right(lst, target)
    print()
    return None


if __name__ == '__main__':
    # 小さなリストで実行
    small_lists = [[], [1], [1, 2], [1, 3, 5], [2, 4, 6, 8, 10]]
    targets = [-1, 2, 9, 11]
    for target in targets:
        for lst in small_lists:
            run_binary_search_patterns(lst, target)

    # 要素数25のリストで実行
    # even_numbers = [i for i in range(50) if i % 2 == 0]
    # odd_numbers = [i for i in range(50) if i % 2 == 1]
    # numbers_lists = [even_numbers, odd_numbers]
    # targets = [-1, 7, 24, 42, 50]
    # for target in targets:
    #     for lst in numbers_lists:
    #         run_binary_search_patterns(lst, target)
