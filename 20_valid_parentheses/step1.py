# step1

class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_stack = []
        close_to_open = {")":"(", "]":"[", "}":"{"}
        for char in s:
            if char not in "()[]{}":
                continue
            if char in "([{":
                parentheses_stack.append(char)
                continue
            if char in ")]}":
                if not parentheses_stack:
                    return False
                if parentheses_stack.pop() != close_to_open[char]:
                    return False
        if parentheses_stack:
            return False
        return True

"""
・カッコの対応づけ方の選択。
思いついた選択肢と判断理由は次の通り。
1. すべて書き下す if char == "(", if char == ")"... は分岐の数が増えるので大変そう
2. open_parentheses = "([{", close_parentheses = ")]}" はインデックスを経由するので対応付けが曖昧、カッコ以外にも管理したい組が増えると大変になってきそう。
3. keyに右括弧, valueに左括弧を格納するdictを使う。
    1. 条件文でdict.keys(), dict.values() を都度計算するのはもったいなく感じるので "([{" と書き下した
    2. 組が増えた場合は、ループに入るまえに dict.keys(), dict.values() を求めてそれぞれを set() に入れて, `if char in close_X` などとして対応できそう。
と考えて、辞書を選択した。

・return Falseを実行する条件文を2つに分解した。
まとめて書くと80列をオーバーしたため。
PEP8によれば、次のように書いてもいい
```
if (not parentheses_stack or \
        parentheses_stack.pop() != close_to_open[char]):
    return False
```
"""
