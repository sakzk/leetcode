#!/usr/bin/env python3

"""
LeetCodeのサイト上の問題名をコピペして貼り付けると、
pythonの命名規則に沿ったスネークケースに変換し、
クリップボードに保存するGUIプログラム

使い方：
起動すると入力フィールドを備えたウインドウが立ち上がるので、
整形したい文字を入力フィールドにコピペして
"Remove Spaces and Copy to Clipboard" をクリックする。

例：
33. Search in Rotated Sorted Array
-> 33_search_in_rotated_sorted_array

準備：pyperclip モジュールのインストールが必要。
"""

import tkinter as tk
import tkinter.messagebox
import tkinter.ttk as ttk
import pyperclip

def remove_spaces():
    input_text = entry.get()
    result_text = input_text.lower().replace(".", "").replace(" ", "_")
    pyperclip.copy(result_text)
    # tkinter.messagebox.showinfo("Success", f"{result_text}")
    entry.delete(0, tk.END)
    input_text = ""

# ウィンドウを中央に配置する関数
def center_window(window, width=400, height=200):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

# メインウインドウを作成
window = tk.Tk()
window.title("Remove Spaces and Copy to Clipboard")

# ウィンドウを中央に配置
center_window(window)

# 入力用のラベルとエントリウィジェットを作成する
label = tk.Label(window, text="Enter text:")
label.pack(pady=30)
entry = tk.Entry(window)
entry.pack(padx=10, pady=5)

# スペースの削除とクリップボードへのコピーをトリガーするボタンを作成する
button = ttk.Button(window, text="Remove Spaces and Copy to Clipboard", command=remove_spaces)
button.pack(pady=10)

# メインループを実行する
window.mainloop()
