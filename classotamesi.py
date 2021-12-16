#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import tkinter
from tkinter.constants import LEFT
from tkinter import messagebox


class Task():
    def __init__(self):
        self.EntryBox = tkinter.Entry(width=20)
        self.CheckBox = tkinter.Checkbutton(text=u'絶対やること１つ')
        self.box_y=0
        self.check_box_y=0

    
    
    def add_box_y(self,DEFAULT_Y):#エントリーボックスのy座標の位置の更新
        self.box_y+=DEFAULT_Y
        return self.box_y
    
    def add_check_box_y(self,DEFAULT_Y):#チェックボックスのy座標の位置の更新
        self.check_box_y+=DEFAULT_Y    
        return self.check_box_y

    def create_widgets(self,DEFAULT_Y):#タスクのy座標の更新
      self.add_box_y(DEFAULT_Y)
      self.add_check_box_y(DEFAULT_Y)

    def MakeBox(self,DEFAULT_Y,DEFAULTENTRYBOX_X):
    #入力ボックスの作成
      it_box_y=self.add_box_y(DEFAULT_Y)
    
      #EditBox = tkinter.Entry(width=20)
      self.EntryBox.insert(tkinter.END,"・")
      self.EntryBox.place(x=DEFAULTENTRYBOX_X, y=it_box_y)
    
    def MakeCheckBox(self,DEFAULTCHECKBOX_X,DEFAULT_Y):
      #チェックボックスの作成
      it_check_y=self.add_check_box_y(DEFAULT_Y)
      #print(it_check_y)
      #CheckBox = tkinter.Checkbutton(text=u'絶対やること１つ')
      self.CheckBox.place(x=DEFAULTCHECKBOX_X,y=it_check_y)
    
    def MakeTask(self,DEFAULT_Y,DEFAULTENTRYBOX_X,DEFAULTCHECKBOX_X):
      self.MakeBox(DEFAULT_Y,DEFAULTENTRYBOX_X)
      self.MakeCheckBox(DEFAULTCHECKBOX_X,DEFAULT_Y)




class Application(tkinter.Frame):
  def __init__(self, master = None):
    super().__init__(master)
    self.Task = Task()
    # self.pack()
    
    self.master.title(u"Software Title")###ここから
    self.master.geometry("400x300")
    self.EDITDEFAULT_X=160
    self.EDITDEFAULT_Y=20
    self.DEFAULTENTRYBOX_X=130 #最初の入力ボックスのx座標
    self.DEFAULT_Y=40 #最初のエントリーボックスとチェックボックスのy座標
    self.DEFAULTCHECKBOX_X=0
    #self.taskList = []
      
    #ラベル
    self.Static1 = tkinter.Label(text=u'Do it now!')
    self.Static1.place(x=self.EDITDEFAULT_X,y=self.EDITDEFAULT_Y)

    #ボタン
    self.Button = tkinter.Button(text=u'押すなよ！絶対押すなよ！')
    self.Button.bind("<Button-1>",self.Task.MakeTask(self.DEFAULT_Y,self.DEFAULTENTRYBOX_X,self.DEFAULTCHECKBOX_X)) 
    #左クリック（<Button-1>）されると，DeleteEntryValue関数を呼び出すようにバインド
    self.Button.place(x=0,y=0)

    

def main():
  root = tkinter.Tk()
  app = Application(master = root)
  app.mainloop()###ここまで実行内容

if __name__ == "__main__":
  main()