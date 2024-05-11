from typing import List
from collections import deque

def permute(nums: List[int]) -> List[List[int]]:
    print("==========================================")
    print("Input Items:", nums)
    result_permutations = []
    state_queue = deque()
    enqueued_index = 0
    root_state = ([], nums, enqueued_index) # State is a tuple of permutation and remaining_nums.
    enqueued_index += 1
    state_queue.append(root_state)
    print("Initial State Stack:", state_queue)
    called_index = 0
    while state_queue:
        current_state = state_queue.popleft()
        print("dequeued State", called_index, ":", current_state)
        called_index += 1
        permutation = current_state[0]
        remaining_nums = current_state[1]
        if not remaining_nums:
            result_permutations.append(permutation)
            print("Reached Leaf State:", current_state)
        else:
            print("Stack Before Pushing:", state_queue)
            state_derived_from_dequeued_state = [] # for printing all derived state
            for num in remaining_nums:
                # Deep copy to duplicate the state
                next_permutation = permutation.copy()
                next_remaining_nums = remaining_nums.copy()
                # generating one derived state and pushing it to statestack
                next_permutation.append(num)
                next_remaining_nums.remove(num)
                new_state = (next_permutation, next_remaining_nums, enqueued_index)
                state_queue.append(new_state)
                enqueued_index += 1
                state_derived_from_dequeued_state.append(new_state)
                print("enqueued State:", new_state)
            print("All States Derived from dequeued State:", state_derived_from_dequeued_state)
            print("Stack After  Pushing:", state_queue)
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
Initial State Stack: deque([([], [], 0)])
dequeued State 0 : ([], [], 0)
Reached Leaf State: ([], [], 0)
Result Permutations: [[]]
"""

# permute([1])
"""
==========================================
Input Items: [1]
Initial State Stack: deque([([], [1], 0)])
dequeued State 0 : ([], [1], 0)
Stack Before Pushing: deque([])
enqueued State: ([1], [], 1)
All States Derived from dequeued State: [([1], [], 1)]
Stack After  Pushing: deque([([1], [], 1)])
dequeued State 1 : ([1], [], 1)
Reached Leaf State: ([1], [], 1)
Result Permutations: [[1]]
"""

# permute([1, 2])
"""
==========================================
Input Items: [1, 2]
Initial State Stack: deque([([], [1, 2], 0)])
dequeued State 0 : ([], [1, 2], 0)
Stack Before Pushing: deque([])
enqueued State: ([1], [2], 1)
enqueued State: ([2], [1], 2)
All States Derived from dequeued State: [([1], [2], 1), ([2], [1], 2)]
Stack After  Pushing: deque([([1], [2], 1), ([2], [1], 2)])
dequeued State 1 : ([1], [2], 1)
Stack Before Pushing: deque([([2], [1], 2)])
enqueued State: ([1, 2], [], 3)
All States Derived from dequeued State: [([1, 2], [], 3)]
Stack After  Pushing: deque([([2], [1], 2), ([1, 2], [], 3)])
dequeued State 2 : ([2], [1], 2)
Stack Before Pushing: deque([([1, 2], [], 3)])
enqueued State: ([2, 1], [], 4)
All States Derived from dequeued State: [([2, 1], [], 4)]
Stack After  Pushing: deque([([1, 2], [], 3), ([2, 1], [], 4)])
dequeued State 3 : ([1, 2], [], 3)
Reached Leaf State: ([1, 2], [], 3)
dequeued State 4 : ([2, 1], [], 4)
Reached Leaf State: ([2, 1], [], 4)
Result Permutations: [[1, 2], [2, 1]]
"""

# permute([1, 2, 3])
"""
==========================================
Input Items: [1, 2, 3]
Initial State Stack: deque([([], [1, 2, 3], 0)])
dequeued State 0 : ([], [1, 2, 3], 0)
Stack Before Pushing: deque([])
enqueued State: ([1], [2, 3], 1)
enqueued State: ([2], [1, 3], 2)
enqueued State: ([3], [1, 2], 3)
All States Derived from dequeued State: [([1], [2, 3], 1), ([2], [1, 3], 2), ([3], [1, 2], 3)]
Stack After  Pushing: deque([([1], [2, 3], 1), ([2], [1, 3], 2), ([3], [1, 2], 3)])
dequeued State 1 : ([1], [2, 3], 1)
Stack Before Pushing: deque([([2], [1, 3], 2), ([3], [1, 2], 3)])
enqueued State: ([1, 2], [3], 4)
enqueued State: ([1, 3], [2], 5)
All States Derived from dequeued State: [([1, 2], [3], 4), ([1, 3], [2], 5)]
Stack After  Pushing: deque([([2], [1, 3], 2), ([3], [1, 2], 3), ([1, 2], [3], 4), ([1, 3], [2], 5)])
dequeued State 2 : ([2], [1, 3], 2)
Stack Before Pushing: deque([([3], [1, 2], 3), ([1, 2], [3], 4), ([1, 3], [2], 5)])
enqueued State: ([2, 1], [3], 6)
enqueued State: ([2, 3], [1], 7)
All States Derived from dequeued State: [([2, 1], [3], 6), ([2, 3], [1], 7)]
Stack After  Pushing: deque([([3], [1, 2], 3), ([1, 2], [3], 4), ([1, 3], [2], 5), ([2, 1], [3], 6), ([2, 3], [1], 7)])
dequeued State 3 : ([3], [1, 2], 3)
Stack Before Pushing: deque([([1, 2], [3], 4), ([1, 3], [2], 5), ([2, 1], [3], 6), ([2, 3], [1], 7)])
enqueued State: ([3, 1], [2], 8)
enqueued State: ([3, 2], [1], 9)
All States Derived from dequeued State: [([3, 1], [2], 8), ([3, 2], [1], 9)]
Stack After  Pushing: deque([([1, 2], [3], 4), ([1, 3], [2], 5), ([2, 1], [3], 6), ([2, 3], [1], 7), ([3, 1], [2], 8), ([3, 2], [1], 9)])
dequeued State 4 : ([1, 2], [3], 4)
Stack Before Pushing: deque([([1, 3], [2], 5), ([2, 1], [3], 6), ([2, 3], [1], 7), ([3, 1], [2], 8), ([3, 2], [1], 9)])
enqueued State: ([1, 2, 3], [], 10)
All States Derived from dequeued State: [([1, 2, 3], [], 10)]
Stack After  Pushing: deque([([1, 3], [2], 5), ([2, 1], [3], 6), ([2, 3], [1], 7), ([3, 1], [2], 8), ([3, 2], [1], 9), ([1, 2, 3], [], 10)])
dequeued State 5 : ([1, 3], [2], 5)
Stack Before Pushing: deque([([2, 1], [3], 6), ([2, 3], [1], 7), ([3, 1], [2], 8), ([3, 2], [1], 9), ([1, 2, 3], [], 10)])
enqueued State: ([1, 3, 2], [], 11)
All States Derived from dequeued State: [([1, 3, 2], [], 11)]
Stack After  Pushing: deque([([2, 1], [3], 6), ([2, 3], [1], 7), ([3, 1], [2], 8), ([3, 2], [1], 9), ([1, 2, 3], [], 10), ([1, 3, 2], [], 11)])
dequeued State 6 : ([2, 1], [3], 6)
Stack Before Pushing: deque([([2, 3], [1], 7), ([3, 1], [2], 8), ([3, 2], [1], 9), ([1, 2, 3], [], 10), ([1, 3, 2], [], 11)])
enqueued State: ([2, 1, 3], [], 12)
All States Derived from dequeued State: [([2, 1, 3], [], 12)]
Stack After  Pushing: deque([([2, 3], [1], 7), ([3, 1], [2], 8), ([3, 2], [1], 9), ([1, 2, 3], [], 10), ([1, 3, 2], [], 11), ([2, 1, 3], [], 12)])
dequeued State 7 : ([2, 3], [1], 7)
Stack Before Pushing: deque([([3, 1], [2], 8), ([3, 2], [1], 9), ([1, 2, 3], [], 10), ([1, 3, 2], [], 11), ([2, 1, 3], [], 12)])
enqueued State: ([2, 3, 1], [], 13)
All States Derived from dequeued State: [([2, 3, 1], [], 13)]
Stack After  Pushing: deque([([3, 1], [2], 8), ([3, 2], [1], 9), ([1, 2, 3], [], 10), ([1, 3, 2], [], 11), ([2, 1, 3], [], 12), ([2, 3, 1], [], 13)])
dequeued State 8 : ([3, 1], [2], 8)
Stack Before Pushing: deque([([3, 2], [1], 9), ([1, 2, 3], [], 10), ([1, 3, 2], [], 11), ([2, 1, 3], [], 12), ([2, 3, 1], [], 13)])
enqueued State: ([3, 1, 2], [], 14)
All States Derived from dequeued State: [([3, 1, 2], [], 14)]
Stack After  Pushing: deque([([3, 2], [1], 9), ([1, 2, 3], [], 10), ([1, 3, 2], [], 11), ([2, 1, 3], [], 12), ([2, 3, 1], [], 13), ([3, 1, 2], [], 14)])
dequeued State 9 : ([3, 2], [1], 9)
Stack Before Pushing: deque([([1, 2, 3], [], 10), ([1, 3, 2], [], 11), ([2, 1, 3], [], 12), ([2, 3, 1], [], 13), ([3, 1, 2], [], 14)])
enqueued State: ([3, 2, 1], [], 15)
All States Derived from dequeued State: [([3, 2, 1], [], 15)]
Stack After  Pushing: deque([([1, 2, 3], [], 10), ([1, 3, 2], [], 11), ([2, 1, 3], [], 12), ([2, 3, 1], [], 13), ([3, 1, 2], [], 14), ([3, 2, 1], [], 15)])
dequeued State 10 : ([1, 2, 3], [], 10)
Reached Leaf State: ([1, 2, 3], [], 10)
dequeued State 11 : ([1, 3, 2], [], 11)
Reached Leaf State: ([1, 3, 2], [], 11)
dequeued State 12 : ([2, 1, 3], [], 12)
Reached Leaf State: ([2, 1, 3], [], 12)
dequeued State 13 : ([2, 3, 1], [], 13)
Reached Leaf State: ([2, 3, 1], [], 13)
dequeued State 14 : ([3, 1, 2], [], 14)
Reached Leaf State: ([3, 1, 2], [], 14)
dequeued State 15 : ([3, 2, 1], [], 15)
Reached Leaf State: ([3, 2, 1], [], 15)
Result Permutations: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
"""
