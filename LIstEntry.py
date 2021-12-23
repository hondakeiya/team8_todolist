#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import tkinter as tk
from tkinter.constants import LEFT
from tkinter import messagebox

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
    
    #全体ラベル
    self.Static1 = tk.Label(text=u'Do it now!')
    self.Static1.place(x=160,y=0)

    #リスト名前のラベル
    self.Static2 = tk.Label(text=u'・やること')
    self.Static2.place(x=20,y=50)

    #リスト詳細のラベル
    self.Static3 = tk.Label(text=u'・やることの詳細')
    self.Static3.place(x=20,y=80)

    def MakeBox(text1):
    #入力ボックスの作成
        self.ListBox1.insert(tk.END, text1)
    
    def MakeExplanation(text2):
        self.ListBox2.insert(tk.END, text2)
    
    def deleteSelectedList():#削除関数
        selectedIndex = tk.ACTIVE
        self.ListBox1.delete(selectedIndex)
        self.ListBox2.delete(selectedIndex)
    
    def MakeTask(text1,text2):
      MakeBox(text1)
      MakeExplanation(text2)
    #   MakeCheckBox()
    
    #リストの名前設定用のEntryBox
    self.Entry1 = tk.Entry(width=20)
    self.Entry1.insert(tk.END, u'挿入する文字列')
    self.Entry1.place(x=200,y=50)

    #リストの詳細記述用のEntryBox
    self.Entry2 = tk.Entry(width=20)
    self.Entry2.insert(tk.END, u'詳細')
    self.Entry2.place(x=200,y=80)

    #ボタン
    self.Button1 = tk.Button(text=u'押すなよ！絶対押すなよ！', command=lambda:MakeTask(self.Entry1.get(),self.Entry2.get()))
    self.Button1.place(x=20,y=20)
    
    self.Button2 = tk.Button(text=u'てめえはもう用済みだ!', command=lambda:deleteSelectedList())
    self.Button2.place(x=200,y=20)
    
    #Todoリスト作成
    self.ListBox1 = tk.Listbox(width=15, height=15)
    self.ListBox1.place(x=10,y=120)
    
    self.ListBox2 = tk.Listbox(width=15, height=15)
    self.ListBox2.place(x=150,y=120)

def main():
  root = tk.Tk()
  app = Application(master = root)
  def on_closing():
   if messagebox.askokcancel("Quit", "Do you want to quit?"):
    root.destroy()

  root.protocol("WM_DELETE_WINDOW", on_closing)
  app.mainloop()

if __name__ == "__main__":
  main()