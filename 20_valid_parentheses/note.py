"""
想定していない入力に対する処理：
https://github.com/rm3as/code_interview/pull/4/files
https://discord.com/channels/1084280443945353267/1225849404037009609/1231649668442882109

命名関連：
予約語は変数名に使わない：https://docs.python.org/3/reference/lexical_analysis.html#keywords
予約語との被りを避けるための 変数名末尾の`_` ：https://peps.python.org/pep-0008/#descriptive-naming-styles
    google python style guide には 同様の記法についての言及が見当たらなかった https://google.github.io/styleguide/
カッコの名前 (parentheses と brackets で迷ったら) ：https://en.wikipedia.org/wiki/Bracket

dictionary関連:
keys(), values(), items()による要素の取り出しについて:
  これらのメソッドの結果には `in`が使える。
  reversed が使えるのは3.8から。dict_itemsは組をタプルで包んだもの。開いたものではない。
  https://docs.python.org/3/library/stdtypes.html#dictionary-view-objects
  items()が [key1, value1, key2, value2...] を作ると思いこんでデバッグに苦労した。

deque関連：
dequeの使い方。rotateは左方向が正。列の先頭が後ろに戻るイメージ。：https://docs.python.org/3/library/collections.html#collections.deque
pythonのdeque は doubley-linked list。ただし、要素一つ一つがノードなのではなく、固定長のブロック単位でまとまっている。
  (ブロックあたりのオブジェクトの数は、BLOCKLEN = 64で定義されている) これによりmalloc(), free()の呼び出しが減り、データの局所性も改善する。
  https://github.com/python/cpython/blob/1b293b60067f6f4a95984d064ce0f6b6d34c1216/Modules/_collectionsmodule.c#L33
ahayasiさんの deque コードリーディングのメモ：https://discord.com/channels/1084280443945353267/1200089668901937312/1235931317317799957
(現状自分は、ソースのドキュメント部分と手持ちの教科書的な知識を照らし合わせてふーんと思った程度。まだサクッと理解できる感じではない。)
先頭要素の編集が多いならlistではなくdequeを使った方がいい。(listは可変長配列なので先頭側の削除、挿入が重い)

条件文関連：
演算子の優先順位一覧：https://docs.python.org/3/reference/expressions.html#operator-precedence
条件式内での改行・インデントのフォーマット：https://peps.python.org/pep-0008/#indentation
"""
