import datetime
import tkinter as tk
from tkinter import messagebox
import time
from pygame import mixer #pygame が必要





class Application(tk.Frame):
  def __init__(self, master = None):
    super().__init__(master)
    
    self.master.title(u"Software Title")###ここから
    self.master.geometry("400x500")
    self.Things_To_Do_list = [2022, 1, 12, 20]#やるべき事の年、月、日、時のリスト
    
    self.create_widgets()

  # Create Widgets function
  def create_widgets(self):     

    #mt_Fuji = tk.PhotoImage(file='修造.png')



    mixer.init()        #初期化
    mixer.music.load("shuzo5.mp3")  #音声ファイルのパスを入れて読み込む
    

    def syuzo(tasknumber):
        tasktime = datetime.datetime(self.Things_To_Do_list[tasknumber],
        self.Things_To_Do_list[tasknumber+1],self.Things_To_Do_list[tasknumber+2],
        self.Things_To_Do_list[tasknumber+3])
        if tasktime == datetime.datetime.today():
            messagebox.showinfo('いいのか諦めて...','お前は富士山だ') #ここで修造 
            mixer.music.play(1)  #再生回数を指定して再生
            time.sleep(0.01)  #これ入れないと、一瞬で再生されたことになるかも。引数は短い秒数で良い。
        else:
            messagebox.showinfo('焦らない焦らない','一休み一休み')
            mixer.music.play(1)  #再生回数を指定して再生
            time.sleep(0.01)  #これ入れないと、一瞬で再生されたことになるかも。引数は短い秒数で良い。

    

    self.Button1 = tk.Button(text=u'もっと熱くなれよ！', 
    command=lambda:syuzo(0))
    self.Button1.place(x=20,y=20)        


def main():
  root = tk.Tk()
  app = Application(master = root)
  app.mainloop()

if __name__ == "__main__":
  main()    