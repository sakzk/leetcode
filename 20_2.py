# step2−1

class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_stack = []
        close_to_open = {")":"(", "]":"[", "}":"{"}
        for char in s:
            if char not in "()[]{}":
                pass
            elif char in "([{":
                parentheses_stack.append(char)
            else:# iff char in ")]}":
                if not parentheses_stack or parentheses_stack.pop() != close_to_open[char]:
                    return False
        if parentheses_stack:
            return False
        return True

"""
修正点：
- if-continueが3つ並んでいたのを if-elif-elseに書き換えた
    - 3つの条件文が排反なので書き換えてみたが、elseを使うとむしろ排反であることが伝わりにくいと感じた。
"""

# step2-2
class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_stack = []
        close_to_open = {")":"(", "]":"[", "}":"{"}
        open_brackets = set(close_to_open.values())
        close_brackets = set(close_to_open.keys())
        brackets = set()
        for close, open_ in close_to_open.items():
            brackets.add(close)
            brackets.add(_open)

        for char in s:
            if char not in brackets:
                pass
            elif char in open_brackets:
                parentheses_stack.append(char)
            else: # iff char in open_brackets
                if not parentheses_stack or parentheses_stack.pop() != close_to_open[char]:
                    return False
        if parentheses_stack:
            return False
        return True
"""
機能の拡張
- `char in "文字列リテラル"` を書き換えた。
    - close_to_open の要素の key, value が2文字以上で構成される場合にも対応するため。
    - `in` の存在判定は、要素数が少ないとき、set() ではなく list() のほうが早いはず。
        - set() はハッシュの計算を行い、list()は線形探索を行うため

変数名:
- `for close, open_ in close_to_open.items():`
    - close, open_ は for 文でしか使わないので open_bracket を省略して open にしてみたが、組み込み関数の open()と被るので、アンダースコアをつけた。
    - 参照：https://peps.python.org/pep-0008/#descriptive-naming-styles
"""
