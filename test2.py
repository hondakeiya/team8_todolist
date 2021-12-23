#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import tkinter as tk
from tkinter.constants import LEFT

class Application(tk.Frame):
  def __init__(self, master = None):
    super().__init__(master)
    # self.pack()
    
    self.master.title(u"Software Title")###ここから
    self.master.geometry("400x500")
    self.EDITDEFAULT_X=160
    self.EDITDEFAULT_Y=20
    self.DEFAULTENTRYBOX_X=130 #最初の入力ボックスのx座標
    self.DEFAULT_Y=40 #最初の入力ボックスのy座標
    self.DEFAULTCHECKBOX_X=0
    
    self.create_widgets()

  # Create Widgets function
  def create_widgets(self):
    
    #ラベル
    self.Static1 = tk.Label(text=u'Do it now!')
    self.Static1.place(x=160,y=0)
    
    def MakeBox():
    #入力ボックスの作成
        self.ListBox1.insert(tk.END, '絶対やること')
    
    def deleteSelectedList():#削除関数
        selectedIndex = tk.ACTIVE
        self.ListBox1.delete(selectedIndex)
    
    def MakeTask():
      MakeBox()
    #   MakeCheckBox()

    #ボタン
    self.Button1 = tk.Button(text=u'押すなよ！絶対押すなよ！', command=lambda:MakeBox())
    self.Button1.place(x=20,y=20)
    
    self.Button2 = tk.Button(text=u'てめえはもう用済みだ!', command=lambda:deleteSelectedList())
    self.Button2.place(x=200,y=20)
    
    #Todoリスト作成
    self.ListBox1 = tk.Listbox(width=15, height=15)
    self.ListBox1.place(x=10,y=100)

def main():
  root = tk.Tk()
  app = Application(master = root)
  app.mainloop()

if __name__ == "__main__":
  main()