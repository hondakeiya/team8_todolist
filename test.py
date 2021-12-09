#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import tkinter
from tkinter.constants import LEFT
from tkinter import ttk
class Application(tkinter.Frame):
  def _init_(self,master):
    # super().__init__(master)
    # self.pack()
    
    self.master.title(u"Software Title")###ここから
    self.master.geometry("400x300")
    self.EDITDEFAULT_X=160
    self.EDITDEFAULT_Y=20
    self.DEFAULTENTRYBOX_X=130 #最初の入力ボックスのx座標
    self.DEFAULTENTRYBOX_Y=40 #最初の入力ボックスのy座標
    self.DEFAULTCHECKBOX_X=0
    self.DEFAULTCHECKBOX_Y=40
    
    self.box_y=0
    self.check_box_y=0
    
    self.create_widgets()

  # Create Widgets function
  def create_widgets(self):
      pass


def main():
  root = tkinter.Tk()
  app = Application(master = root)
  app.mainloop()###ここまで実行内容

if __name__ == "__main__":
  main()