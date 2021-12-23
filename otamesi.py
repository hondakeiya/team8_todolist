#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import tkinter
from tkinter.constants import LEFT



root = tkinter.Tk()
root.title(u"Software Title")###ここから
root.geometry("400x300")
EDITDEFAULT_X=160
EDITDEFAULT_Y=20
DEFAULTENTRYBOX_X=130 #最初の入力ボックスのx座標
DEFAULTENTRYBOX_Y=40 #最初の入力ボックスのy座標
DEFAULTCHECKBOX_X=0
DEFAULTCHECKBOX_Y=40

box_y=0
check_box_y=0

def add_box_y():
    global box_y
    box_y+=DEFAULTENTRYBOX_Y
    return box_y

def add_check_box_y():
    global check_box_y
    check_box_y+=DEFAULTCHECKBOX_Y    
    return check_box_y





#ラベル
Static1 = tkinter.Label(text=u'Do it now!')
Static1.place(x=EDITDEFAULT_X,y=EDITDEFAULT_Y)

#入力ボックス
#EditBox = tkinter.Entry(width=20)
#EditBox.insert(tkinter.END,"・")
#box_y+=EDITDEFAULT_Y
#EditBox.place(x=DEFAULTENTRYBOX_X, y=box_y)


#CheckBox = tkinter.Checkbutton(text=u'絶対やること１')
#CheckBox.place(x=DEFAULTCHECKBOX_X,y=DEFAULTCHECKBOX_Y)


def MakeBox(event):
    #入力ボックスの作成
    it_box_y=add_box_y()
    
    EditBox = tkinter.Entry(width=20)
    EditBox.insert(tkinter.END,"・")
    EditBox.place(x=DEFAULTENTRYBOX_X, y=it_box_y)
    

def MakeCheckBox(event):
    #チェックボックスの作成
    it_check_y=add_check_box_y()
    #print(it_check_y)
    CheckBox = tkinter.Checkbutton(text=u'絶対やること１つ')
    CheckBox.place(x=DEFAULTCHECKBOX_X,y=it_check_y)   

def MakeTask(event):
    MakeBox(event)
    MakeCheckBox(event)     

#
# ボタンが押されるとここが呼び出される
#
#def DeleteEntryValue(event):
  #エントリーの中身を削除
  #EditBox.delete(0, tkinter.END)

#ボタン
Button = tkinter.Button(text=u'熱くなれよ！')
Button.bind("<Button-1>",MakeTask) 
#Button.bind("<Button-2>",MakeCheckBox) 
#左クリック（<Button-1>）されると，DeleteEntryValue関数を呼び出すようにバインド

Button.place(x=0,y=0)


#CheckBox = tkinter.Checkbutton(text=u'絶対やること１')
#CheckBox.pack()

#CheckBox = tkinter.Checkbutton(text=u'絶対やること２')
#CheckBox.pack()

#CheckBox = tkinter.Checkbutton(text=u'絶対やること３')
#CheckBox.pack()

root.mainloop()###ここまで実行内容