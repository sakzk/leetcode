from typing import List

def permute(nums: List[int]) -> List[List[int]]:
    print("==========================================")
    print("Input Items:", nums)
    result_permutations = []
    state_stack = []
    pushed_index = 0
    root_state = ([], nums, pushed_index) # State is a tuple of permutation and remaining_nums.
    pushed_index += 1
    state_stack.append(root_state)
    print("Initial State Stack:", state_stack)
    called_index = 0
    while state_stack:
        current_state = state_stack.pop()
        print("Popped State", called_index, ":", current_state)
        called_index += 1
        permutation = current_state[0]
        remaining_nums = current_state[1]
        if not remaining_nums:
            result_permutations.append(permutation)
            print("Reached Leaf State:", current_state)
        else:
            print("Stack Before Pushing:", state_stack)
            state_derived_from_popped_state = [] # for printing all derived state
            for num in remaining_nums:
                # Deep copy to duplicate the state
                next_permutation = permutation.copy()
                next_remaining_nums = remaining_nums.copy()
                # generating one derived state and pushing it to statestack
                next_permutation.append(num)
                next_remaining_nums.remove(num)
                new_state = (next_permutation, next_remaining_nums, pushed_index)
                state_stack.append(new_state)
                pushed_index += 1
                state_derived_from_popped_state.append(new_state)
                print("Pushed State:", new_state)
            print("All States Derived from Popped State:", state_derived_from_popped_state)
            print("Stack After  Pushing:", state_stack)
    print("Result Permutations:", result_permutations)
    return result_permutations

permute([])
permute([1])
permute([1, 2])
permute([1, 2, 3])
# permute([1, 2, 3, 4])

# permute([])
"""
==========================================
Input Items: []
Initial State Stack: [([], [], 0)]
Popped State 0 : ([], [], 0)
Reached Leaf State: ([], [], 0)
Result Permutations: [[]]
"""

# permute([1])
"""
==========================================
Input Items: [1]
Initial State Stack: [([], [1], 0)]
Popped State 0 : ([], [1], 0)
Stack Before Pushing: []
Pushed State: ([1], [], 1)
All States Derived from Popped State: [([1], [], 1)]
Stack After  Pushing: [([1], [], 1)]
Popped State 1 : ([1], [], 1)
Reached Leaf State: ([1], [], 1)
Result Permutations: [[1]]
"""

# permute([1, 2])
"""
==========================================
Input Items: [1, 2]
Initial State Stack: [([], [1, 2], 0)]
Popped State 0 : ([], [1, 2], 0)
Stack Before Pushing: []
Pushed State: ([1], [2], 1)
Pushed State: ([2], [1], 2)
All States Derived from Popped State: [([1], [2], 1), ([2], [1], 2)]
Stack After  Pushing: [([1], [2], 1), ([2], [1], 2)]
Popped State 1 : ([2], [1], 2)
Stack Before Pushing: [([1], [2], 1)]
Pushed State: ([2, 1], [], 3)
All States Derived from Popped State: [([2, 1], [], 3)]
Stack After  Pushing: [([1], [2], 1), ([2, 1], [], 3)]
Popped State 2 : ([2, 1], [], 3)
Reached Leaf State: ([2, 1], [], 3)
Popped State 3 : ([1], [2], 1)
Stack Before Pushing: []
Pushed State: ([1, 2], [], 4)
All States Derived from Popped State: [([1, 2], [], 4)]
Stack After  Pushing: [([1, 2], [], 4)]
Popped State 4 : ([1, 2], [], 4)
Reached Leaf State: ([1, 2], [], 4)
Result Permutations: [[2, 1], [1, 2]]
"""

# permute([1, 2, 3])
"""
==========================================
Input Items: [1, 2, 3]
Initial State Stack: [([], [1, 2, 3], 0)]
Popped State 0 : ([], [1, 2, 3], 0)
Stack Before Pushing: []
Pushed State: ([1], [2, 3], 1)
Pushed State: ([2], [1, 3], 2)
Pushed State: ([3], [1, 2], 3)
All States Derived from Popped State: [([1], [2, 3], 1), ([2], [1, 3], 2), ([3], [1, 2], 3)]
Stack After  Pushing: [([1], [2, 3], 1), ([2], [1, 3], 2), ([3], [1, 2], 3)]
Popped State 1 : ([3], [1, 2], 3)
Stack Before Pushing: [([1], [2, 3], 1), ([2], [1, 3], 2)]
Pushed State: ([3, 1], [2], 4)
Pushed State: ([3, 2], [1], 5)
All States Derived from Popped State: [([3, 1], [2], 4), ([3, 2], [1], 5)]
Stack After  Pushing: [([1], [2, 3], 1), ([2], [1, 3], 2), ([3, 1], [2], 4), ([3, 2], [1], 5)]
Popped State 2 : ([3, 2], [1], 5)
Stack Before Pushing: [([1], [2, 3], 1), ([2], [1, 3], 2), ([3, 1], [2], 4)]
Pushed State: ([3, 2, 1], [], 6)
All States Derived from Popped State: [([3, 2, 1], [], 6)]
Stack After  Pushing: [([1], [2, 3], 1), ([2], [1, 3], 2), ([3, 1], [2], 4), ([3, 2, 1], [], 6)]
Popped State 3 : ([3, 2, 1], [], 6)
Reached Leaf State: ([3, 2, 1], [], 6)
Popped State 4 : ([3, 1], [2], 4)
Stack Before Pushing: [([1], [2, 3], 1), ([2], [1, 3], 2)]
Pushed State: ([3, 1, 2], [], 7)
All States Derived from Popped State: [([3, 1, 2], [], 7)]
Stack After  Pushing: [([1], [2, 3], 1), ([2], [1, 3], 2), ([3, 1, 2], [], 7)]
Popped State 5 : ([3, 1, 2], [], 7)
Reached Leaf State: ([3, 1, 2], [], 7)
Popped State 6 : ([2], [1, 3], 2)
Stack Before Pushing: [([1], [2, 3], 1)]
Pushed State: ([2, 1], [3], 8)
Pushed State: ([2, 3], [1], 9)
All States Derived from Popped State: [([2, 1], [3], 8), ([2, 3], [1], 9)]
Stack After  Pushing: [([1], [2, 3], 1), ([2, 1], [3], 8), ([2, 3], [1], 9)]
Popped State 7 : ([2, 3], [1], 9)
Stack Before Pushing: [([1], [2, 3], 1), ([2, 1], [3], 8)]
Pushed State: ([2, 3, 1], [], 10)
All States Derived from Popped State: [([2, 3, 1], [], 10)]
Stack After  Pushing: [([1], [2, 3], 1), ([2, 1], [3], 8), ([2, 3, 1], [], 10)]
Popped State 8 : ([2, 3, 1], [], 10)
Reached Leaf State: ([2, 3, 1], [], 10)
Popped State 9 : ([2, 1], [3], 8)
Stack Before Pushing: [([1], [2, 3], 1)]
Pushed State: ([2, 1, 3], [], 11)
All States Derived from Popped State: [([2, 1, 3], [], 11)]
Stack After  Pushing: [([1], [2, 3], 1), ([2, 1, 3], [], 11)]
Popped State 10 : ([2, 1, 3], [], 11)
Reached Leaf State: ([2, 1, 3], [], 11)
Popped State 11 : ([1], [2, 3], 1)
Stack Before Pushing: []
Pushed State: ([1, 2], [3], 12)
Pushed State: ([1, 3], [2], 13)
All States Derived from Popped State: [([1, 2], [3], 12), ([1, 3], [2], 13)]
Stack After  Pushing: [([1, 2], [3], 12), ([1, 3], [2], 13)]
Popped State 12 : ([1, 3], [2], 13)
Stack Before Pushing: [([1, 2], [3], 12)]
Pushed State: ([1, 3, 2], [], 14)
All States Derived from Popped State: [([1, 3, 2], [], 14)]
Stack After  Pushing: [([1, 2], [3], 12), ([1, 3, 2], [], 14)]
Popped State 13 : ([1, 3, 2], [], 14)
Reached Leaf State: ([1, 3, 2], [], 14)
Popped State 14 : ([1, 2], [3], 12)
Stack Before Pushing: []
Pushed State: ([1, 2, 3], [], 15)
All States Derived from Popped State: [([1, 2, 3], [], 15)]
Stack After  Pushing: [([1, 2, 3], [], 15)]
Popped State 15 : ([1, 2, 3], [], 15)
Reached Leaf State: ([1, 2, 3], [], 15)
Result Permutations: [[3, 2, 1], [3, 1, 2], [2, 3, 1], [2, 1, 3], [1, 3, 2], [1, 2, 3]]
"""
