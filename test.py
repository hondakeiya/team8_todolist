#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import tkinter as tk
from tkinter.constants import LEFT
from dateutil import relativedelta
from datetime import date,timedelta

class Application(tk.Frame):
  def __init__(self, master = None):
    super().__init__(master)
    
    self.master.title(u"Software Title")###ここから
    self.master.geometry("400x500")
    
    self.create_widgets()

  # Create Widgets function
  def create_widgets(self):
    
    #ラベル
    self.Static1 = tk.Label(text=u'Do it now!')
    self.Static1.place(x=160,y=0)
    
    def MakeBox(text):
    #入力ボックスの作成
        self.ListBox1.insert(tk.END, text)
    
    def MakeExplanation(text):
        self.ListBox2.insert(tk.END, text)
    
    def deleteSelectedList():#削除関数
        selectedIndex = tk.ACTIVE
        self.ListBox1.delete(selectedIndex)
        self.ListBox2.delete(selectedIndex)
        self.ListBox3.delete(selectedIndex)
    
    def MakeDeadlineSetting(text1,text2,text3):#期限設定
      self.ListBox3.insert(tk.END, text1+"/"+text2+"/"+text3)
      int1=int(text1)
      int2=int(text2)
      int3=int(text3)
      d = date(int1,int2,int3)
      yd = d - timedelta(days=1)
      print(d)
      print(yd)
      
      
      
      
    
    def MakeTask(text1,text2,text3,text4,text5):
      MakeBox(text1)
      MakeExplanation(text2)
      MakeDeadlineSetting(text3,text4,text5)
    
    # entryboxとそのラベル
    self.Entry1 = tk.Entry(width=10)
    self.Entry1.insert(tk.END, u'title')
    self.Entry1.place(x=120,y=50)
    self.label2 = tk.Label(text="絶対にやる事")
    self.label2.place(x=20,y=50)
    
    self.Entry2 = tk.Entry(width=10)
    self.Entry2.insert(tk.END, u'kwsk')
    self.Entry2.place(x=120,y=80)
    self.label3 = tk.Label(text="詳細")
    self.label3.place(x=20,y=80)
    
    self.Entry3 = tk.Entry(width=4)# 本当はimport dateから持ってきたい
    self.Entry3.insert(tk.END, u'2022')
    self.Entry3.place(x=120,y=110)
    self.Entry4 = tk.Entry(width=2)
    self.Entry4.insert(tk.END, u'1')
    self.Entry4.place(x=170,y=110)
    self.Entry5 = tk.Entry(width=2)
    self.Entry5.insert(tk.END, u'3')
    self.Entry5.place(x=200,y=110)
    self.label4 = tk.Label(text="提出日")
    self.label4.place(x=20,y=110)

    #ボタン
    self.Button1 = tk.Button(text=u'押すなよ！絶対押すなよ！', 
    command=lambda:MakeTask(self.Entry1.get(),self.Entry2.get(),
    self.Entry3.get(),self.Entry4.get(),self.Entry5.get()))
    self.Button1.place(x=20,y=20)
    
    self.Button2 = tk.Button(text=u'てめえはもう用済みだ!', command=lambda:deleteSelectedList())
    self.Button2.place(x=200,y=20)
    
    #Todoリスト作成
    self.ListBox1 = tk.Listbox(width=15, height=15)
    self.ListBox1.place(x=10,y=150)
    
    self.ListBox2 = tk.Listbox(width=15, height=15)
    self.ListBox2.place(x=150,y=150)
    
    self.ListBox3 = tk.Listbox(width=10, height=15)
    self.ListBox3.place(x=290,y=150)

def main():
  root = tk.Tk()
  app = Application(master = root)
  app.mainloop()

if __name__ == "__main__":
  main()