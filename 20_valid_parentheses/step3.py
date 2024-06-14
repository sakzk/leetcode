# step3
# いちばんタイプ量が多い実装で6'30
from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        brackets_stack = deque()
        close_to_open = {")":"(", "]":"[", "}":"{"}
        open_bracket_chars = set(close_to_open.values())
        close_bracket_chars = set(close_to_open.keys())
        all_bracket_chars = set()
        for close, open_ in close_to_open.items():
            all_bracket_chars.add(close)
            all_bracket_chars.add(_open)

        for char in s:
            if char not in all_bracket_chars:
                continue
            if char in open_bracket_chars:
                brackets_stack.append(char)
                continue
            if char in close_bracket_chars:
                if not brackets_stack:
                    return False
                if brackets_stack.pop != close_to_open[char]:
                    return False
        return not brackets_stack

"""
データ構造の変更：
スタックとして deque (double ended queue) を使う。dequeについては、note.pyを参照
stackの頂点の要素を取り出さずに、見るだけなら以下のようにする。
  ```
  peek = brackets_stack[-1]
  if peek != close_to_open[char]:
      return False
  brackets_stack.pop()
  ```

変数名の変更：
parentheses -> brackets: カッコの総称としては、parentheses よりも brackets のほうが良さそうだったため。 (参照) https://en.wikipedia.org/wiki/Bracket

返り値の変更：
  ```
  if not brackets_stack:
      return False
  return True
  ```
は
  ```
  return not brackets_stack
  ```
だけでいい。
"""
