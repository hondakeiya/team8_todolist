#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import tkinter as tk
from tkinter.constants import LEFT
from datetime import date,timedelta
import datetime
import schedule
import time
from pygame import mixer #pygame が必要
import shuzo_onsei #音声再生用

class Application(tk.Frame):
  def __init__(self, master = None):
    super().__init__(master)
    
    self.master.title(u"Software Title")###ここから
    self.master.geometry("400x500")
    self.Things_To_Do_list = []#やるべき事のリスト
    self.create_widgets()
    # schedule.every(1).hour.do(self.create_widget(self.Check_Things_To_Do()))#毎時間処理予定
    self.sc()
    self.MakeTask_Onsei = shuzo_onsei.shuzo_onsei("ganbareyo.mp3") #引数に音声パスを入力して、インスタンス化
  
  def sc(self): # scheduleモジュールにて定期的にタスク状態を確認
    schedule.run_pending()
    self.after(1, self.sc) # 再帰的に実行

  # Create Widgets function
  def create_widgets(self):
    
    #ラベル
    self.Static1 = tk.Label(text=u'Do it now!')
    self.Static1.place(x=160,y=0)
    
    def MakeBox(text):
      self.ListBox1.insert(tk.END, text)
    
    def MakeExplanation(text):
      self.ListBox2.insert(tk.END, text)
    
    def deleteSelectedList():#削除関数
      selectedIndex = tk.ACTIVE
      self.ListBox1.delete(selectedIndex)
      self.ListBox2.delete(selectedIndex)
      self.ListBox3.delete(selectedIndex)
    
    def MakeDeadlineSetting(text1,text2,text3,text4):#期限設定
      self.ListBox3.insert(tk.END, text1+"/"+text2+"/"+text3+"/"+text4+"時")#リストに追加
      self.Things_To_Do_list.append(int(text1))#リストに追加
      self.Things_To_Do_list.append(int(text2))
      self.Things_To_Do_list.append(int(text3))
      self.Things_To_Do_list.append(int(text4))
    
    def MakeTask(text1,text2,text3,text4,text5,text6):
      MakeBox(text1)
      MakeExplanation(text2)
      MakeDeadlineSetting(text3,text4,text5,text6)
      self.MakeTask_Onsei.play(1) #再生回数を指定して音声を再生
    
    def Check_Things_To_Do():
      list_number = int(len(self.Things_To_Do_list)/4)
      for i in range(list_number):
        count = i*4
        if self.dt_now.year == self.Things_To_Do_list[count] and self.dt_now.month == self.Things_To_Do_list[count+1]:
          if self.dt_now.day == self.Things_To_Do_list[count+2] - 1:
            print(i+1+"番目の課題にもっと熱くなれよ!こっちもしじみがトゥルルって頑張ってんだから!")
          if self.dt_now.day == self.Things_To_Do_list[count+2]:
            print(i+1+"番目の課題を諦めんなよ。諦めんなよお前!")
    
    # entryboxとそのラベル
    self.Entry1 = tk.Entry(width=10)
    self.Entry1.insert(tk.END, 'title')
    self.Entry1.place(x=120,y=50)
    self.label2 = tk.Label(text="絶対にやる事")
    self.label2.place(x=20,y=50)
    
    self.Entry2 = tk.Entry(width=10)
    self.Entry2.insert(tk.END, 'kwsk')
    self.Entry2.place(x=120,y=80)
    self.label3 = tk.Label(text="詳細")
    self.label3.place(x=20,y=80)
    
    self.dt_now = datetime.datetime.now()# 現在日時を取得
    self.Entry3 = tk.Entry(width=4)
    self.Entry3.insert(tk.END, self.dt_now.year)#入力欄に今年を挿入
    self.Entry3.place(x=120,y=110)
    self.label5 = tk.Label(text="年")
    self.label5.place(x=170,y=110)
    self.Entry4 = tk.Entry(width=2)
    self.Entry4.insert(tk.END, self.dt_now.month)#入力欄に今月を挿入
    self.Entry4.place(x=190,y=110)
    self.label6 = tk.Label(text="月")
    self.label6.place(x=220,y=110)
    self.Entry5 = tk.Entry(width=2)
    self.Entry5.insert(tk.END, self.dt_now.day)#入力欄に今日を挿入
    self.Entry5.place(x=240,y=110)
    self.label7 = tk.Label(text="日")
    self.label7.place(x=270,y=110)
    self.Entry6 = tk.Entry(width=2)
    self.Entry6.insert(tk.END, self.dt_now.hour)#入力欄に時間を挿入
    self.Entry6.place(x=290,y=110)
    self.label8 = tk.Label(text="時")
    self.label8.place(x=320,y=110)
    self.label4 = tk.Label(text="提出日")
    self.label4.place(x=20,y=110)

    #ボタン
    self.Button1 = tk.Button(text=u'押すなよ!絶対押すなよ!', 
    command=lambda:MakeTask(self.Entry1.get(),self.Entry2.get(),
    self.Entry3.get(),self.Entry4.get(),self.Entry5.get(),self.Entry6.get()))
    self.Button1.place(x=20,y=20)
    
    self.Button2 = tk.Button(text=u'てめえはもう用済みだ!', 
    command=lambda:deleteSelectedList())
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
  schedule.run_pending()
  app.mainloop()

if __name__ == "__main__":
  main()