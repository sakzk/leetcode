# time  complexity: O(n) nの項の最善は最悪の 1/2倍
# space complexity: O(n) nの項の最善は最悪の 1/n倍

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_length = 0
        window_chars = set()
        end = 0 # end finally becomes len(s).
        for begin in range(len(s)):
            while end < len(s) and s[end] not in window_chars:
                window_chars.add(s[end])
                end += 1
            longest_length = max(end - begin, longest_length)
            window_chars.remove(s[begin])
        return longest_length

# 変更点
"""
変数名：
window_chars : 「見たものすべて」を予想させるseen_charsから変更
begin, end : left, rightから変更
    window_begin, window_endも検討したが、簡潔性を選んだ。
    start, stop も検討したが、substring_stop としないと落ち着かなかったので避けた。(自分の慣れの問題かもしれない)
    end が、exclusiveかつ最終的にlen(s)になることをコメントに明示したが、C++では含意されているので読み手によっては冗長と感じるかも。

制御：
beginのループをforループに変更：
    変更前は `while begin < len(s): begin += 1` だった。自明な書き換え
    内側の end の while ループはインデックスの制限の条件に加えて追加の条件があり、rangeに書き換えると制御にフラグを導入することになり複雑になったのでwhileループのまま。

コメント：
最善と最悪の定数倍はビッグO記法を使わずに記述
"""
