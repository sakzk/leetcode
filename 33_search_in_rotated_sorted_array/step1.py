class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            left_val = nums[left]
            mid_val = nums[mid]
            right_val = nums[right]
            if mid_val == target:
                return mid
            elif left_val == target:
                return left
            elif right_val == target:
                return right
            elif left_val < mid_val and left_val < target < mid_val:
                right = mid - 1
            elif left_val < mid_val:
                left = mid + 1
            elif mid_val < right_val and mid_val < target < right_val:
                left = mid + 1
            elif mid_val <= right_val: # < にすると無限ループになる。(left = right がすりぬけるため)
                right = mid - 1
        return -1

""" メモ
# 発想：
- left_val < mid_val < right_val となる場合を除いて、left_val <= mid_val XOR mid_val <= right_val が成り立つ。
    - 5,6分いろいろ試してやっと気づいたが、見た瞬間にサクッと気づくことを期待されているのだろうか。
    - 「たぶんそうだろうけど、本当にそうかすぐにはわからない」というタイプのことはどれぐらい説明できれば証明したことになるのだろうか。
        - そっちに気づけることとちゃんと実装できることは別の能力なので、どうしても思いつかなかったら仮定としてつかっていいか尋ねるとよさそう？

# かかった時間:
- アプローチを考えるのに10分、ひとまず書ききるまで6分、小さな例でテストしつつデバッグに25分、最初から書き直したら書けた。

# 気をつけた点：
- コーディングを始める前に、インデックス、条件式の等号をどうするかまで読み切る。
    - インデックスや条件式をポチポチいじっていつのまにか動いた、になってしまいそうだったので。

# 実装に迷った点
- nums[left], nums[right] を 変数に入れるかどうか
    - pros：区間の端で発見する場合のループする回数が一度減る。書き間違いの可能性が減る。
    - cons：条件分岐が見た目としてかさばる、
    - 選択：変数に入れた。
        - → step2 以降で nums[] を書き下したほうが良いと感じるようになった。
- 分岐をどう書くか。
    - ソートされている区間が左区間／右区間、targetがあるかもしれないのが左区間／右区間の組み合わせで4通りパスがある。
        - ポインタの移動は、left と right のどちらか一方を動かす
    - pros：処理本体の書き間違いが減らせそう。
    - cons：読むときに混乱しそう、順序が大事な場合機械的に結合してもうまく行かないかもしれない
    - 選択：4通りとも別々に書いた。それでも混乱した。
- 条件式をどう書くか？
    - left_val < target < mid_val は left_val < mid_val より狭い条件なので、 left_val < mid_val は必要ないかな、と思ったが、残したままになっている。
        - 実装しているときは left_val < target < mid_val が left_val < mid_val を含んでいるのかあやふやだった。

# よくなかった点
- `elif mid_val <= right_val:` の `<=` を `<` に変えるとなぜだめのか具体例が思いつかなかった。
    - mid == right がすり抜けている。
        - [5, 2, 3] 4 で発生する
        - target が 存在しないときは、`X_val == target` の式の等号が成立しない。
            - 全部にすり抜ける例を思いつくには、全部の条件式を同時に追わないと行けないので頭を使う
    - `=` をつけても間違っていないものには `=` をつけるほうが良い気がする。
        - 条件式を羅列するときは、できるだけ上の条件に引っかけるようにしたい。(その方がはやく脱出できるため)

# 他
- 等号をつける、つけないではなく、上に引っかかっているかどうか。上で引っかかるなら下に書かなくていい。
"""
