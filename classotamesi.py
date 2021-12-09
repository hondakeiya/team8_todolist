#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import tkinter
from tkinter.constants import LEFT
from tkinter import messagebox


class Task():
    def __init__(self):
        self.CheckBox
        self.EntryBox
        self.box_y=0
        self.check_box_y=0

    def create_widgets(self):
    
        def add_box_y():
            self.box_y+=self.DEFAULTENTRYBOX_Y
            return self.box_y
    
        def add_check_box_y():
            self.check_box_y+=self.DEFAULTCHECKBOX_Y    
            return self.check_box_y

    def MakeBox(self,event):
    #入力ボックスの作成
      it_box_y=add_box_y()
    
      EditBox = tkinter.Entry(width=20)
      EditBox.insert(tkinter.END,"・")
      EditBox.place(x=self.DEFAULTENTRYBOX_X, y=it_box_y)
    
    def MakeCheckBox(self,event):
      #チェックボックスの作成
      it_check_y=add_check_box_y()
      #print(it_check_y)
      CheckBox = tkinter.Checkbutton(text=u'絶対やること１つ')
      CheckBox.place(x=self.DEFAULTCHECKBOX_X,y=it_check_y)
    
    def MakeTask(self,event):
      MakeBox(event)
      MakeCheckBox(event)




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
    self.DEFAULTENTRYBOX_Y=40 #最初の入力ボックスのy座標
    self.DEFAULTCHECKBOX_X=0
    self.DEFAULTCHECKBOX_Y=40
    #self.taskList = []
    
    #self.box_y=0
    #self.check_box_y=0
    
    #self.create_widgets()

  # Create Widgets function
  #def create_widgets(self):
    
    #def add_box_y():
      #self.box_y+=self.DEFAULTENTRYBOX_Y
      #return self.box_y
    
    #def add_check_box_y():
      #self.check_box_y+=self.DEFAULTCHECKBOX_Y    
      #return self.check_box_y
    
    #ラベル
    self.Static1 = tkinter.Label(text=u'Do it now!')
    self.Static1.place(x=self.EDITDEFAULT_X,y=self.EDITDEFAULT_Y)

    #入力ボックス
    # self.EditBox = tkinter.Entry()
    # self.EditBox.insert(tkinter.END,"・")
    # self.EditBox.pack()
    
    #def MakeBox(event):
    #入力ボックスの作成
      #it_box_y=add_box_y()
    
      #EditBox = tkinter.Entry(width=20)
      #EditBox.insert(tkinter.END,"・")
      #EditBox.place(x=self.DEFAULTENTRYBOX_X, y=it_box_y)
    
    #def MakeCheckBox(event):
      #チェックボックスの作成
      #it_check_y=add_check_box_y()
      #print(it_check_y)
      #CheckBox = tkinter.Checkbutton(text=u'絶対やること１つ')
      #CheckBox.place(x=self.DEFAULTCHECKBOX_X,y=it_check_y)
    
    #def MakeTask(event):
      #MakeBox(event)
      #MakeCheckBox(event)

    


    


    # ボタンが押されるとここが呼び出される
    # def DeleteEntryValue(event):
    #   #エントリーの中身を削除
    #   self.delete(0, tkinter.END)

    #ボタン
    self.Button = tkinter.Button(text=u'押すなよ！絶対押すなよ！')
    self.Button.bind("<Button-1>",self.task.MakeTask) 
    #左クリック（<Button-1>）されると，DeleteEntryValue関数を呼び出すようにバインド
    self.Button.place(x=0,y=0)

    #チェックボックス
    # self.CheckBox = tkinter.Checkbutton(text=u'絶対やること１')
    # self.CheckBox.place(x=0, y=50)

    # self.CheckBox = tkinter.Checkbutton(text=u'絶対やること２')
    # self.CheckBox.pack()

    # self.CheckBox = tkinter.Checkbutton(text=u'絶対やること３')
    # self.CheckBox.pack()

def main():
  root = tkinter.Tk()
  app = Application(master = root)
  app.mainloop()###ここまで実行内容

if __name__ == "__main__":
  main()