#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import tkinter



root = tkinter.Tk()
root.title(u"Software Title")###ここから
root.geometry("400x300")

#ラベル
Static1 = tkinter.Label(text=u'Do it now!')
Static1.pack()

#入力ボックス
EditBox = tkinter.Entry()
EditBox.insert(tkinter.END,"・")
EditBox.pack()

#
# ボタンが押されるとここが呼び出される
#
def DeleteEntryValue(event):
  #エントリーの中身を削除
  EditBox.delete(0, tkinter.END)

#ボタン
Button = tkinter.Button(text=u'押すなよ！絶対押すなよ！')
Button.bind("<Button-1>",DeleteEntryValue) 
#左クリック（<Button-1>）されると，DeleteEntryValue関数を呼び出すようにバインド
Button.pack()

#チェックボックス
CheckBox = tkinter.Checkbutton(text=u'絶対やること１')
CheckBox.pack()

CheckBox = tkinter.Checkbutton(text=u'絶対やること２')
CheckBox.pack()

CheckBox = tkinter.Checkbutton(text=u'絶対やること３')
CheckBox.pack()

root.mainloop()###ここまで実行内容