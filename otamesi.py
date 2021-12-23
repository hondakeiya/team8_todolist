#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import tkinter
from tkinter.constants import LEFT

class Application(tkinter.Frame):
  def __init__(self, master = None):
    super().__init__(master)
    # self.pack()
    
    self.master.title(u"Software Title")###ここから
    self.master.geometry("400x300")
    self.EDITDEFAULT_X=160
    self.EDITDEFAULT_Y=20
    self.DEFAULTENTRYBOX_X=130 #最初の入力ボックスのx座標
    self.DEFAULT_Y=40 #最初の入力ボックスのy座標
    self.DEFAULTCHECKBOX_X=0
    
    self.box_y=0
    self.check_box_y=0
    
    self.create_widgets()

  # Create Widgets function
  def create_widgets(self):
    
    def get_y():
      return self.box_y
    
    def add_y():
      self.box_y+=self.DEFAULT_Y
      return self.box_y
  
    
    #ラベル
    self.Static1 = tkinter.Label(text=u'Do it now!')
    self.Static1.place(x=self.EDITDEFAULT_X,y=self.EDITDEFAULT_Y)
    
    def MakeBox(event):
    #入力ボックスの作成
      it_box_y=add_y()
    
      EditBox = tkinter.Entry(width=20)
      EditBox.insert(tkinter.END,"・")
      EditBox.place(x=self.DEFAULTENTRYBOX_X, y=it_box_y)
    
    def MakeCheckBox(event):
      #チェックボックスの作成
      it_check_y=get_y()
      #print(it_check_y)
      CheckBox = tkinter.Checkbutton(text=u'絶対やること１つ')
      CheckBox.place(x=self.DEFAULTCHECKBOX_X,y=it_check_y)
    
    def MakeTask(event):
      MakeBox(event)
      MakeCheckBox(event)
    
    def deleteSelectedList():
      selectedIndex = tkinter.ACTIVE
      EditBox.delete(selectedIndex)

    #ボタン
    self.Button = tkinter.Button(text=u'押すなよ！絶対押すなよ！')
    self.Button.bind("<Button-1>",MakeTask)
    
    self.Button = tkinter.Button(text=u'てめえはもう用済みだ!')
    self.Button.bind("<Button-2>",deleteSelectedList)
    #左クリック（<Button-1>）されると，DeleteEntryValue関数を呼び出すようにバインド
    self.Button.place(x=0,y=0)

def main():
  root = tkinter.Tk()
  app = Application(master = root)
  app.mainloop()###ここまで実行内容

if __name__ == "__main__":
  main()