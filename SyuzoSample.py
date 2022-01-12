import datetime
import tkinter as tk
from tkinter import messagebox





class Application(tk.Frame):
  def __init__(self, master = None):
    super().__init__(master)
    
    self.master.title(u"Software Title")###ここから
    self.master.geometry("400x500")
    self.Things_To_Do_list = [2022, 1, 12, 20]#やるべき事の年、月、日、時のリスト
    
    self.create_widgets()

  # Create Widgets function
  def create_widgets(self):       


    

    def syuzoGo(tasknumber):
        tasktime = datetime.datetime(self.Things_To_Do_list[tasknumber],
        self.Things_To_Do_list[tasknumber+1],self.Things_To_Do_list[tasknumber+2],
        self.Things_To_Do_list[tasknumber+3])
        if tasktime == datetime.datetime.today():
            messagebox.showinfo('いいのか諦めて...','お前は富士山だ') #ここで修造 
        else:
            messagebox.showinfo('焦らない焦らない','一休み一休み')

    self.Button1 = tk.Button(text=u'もっと熱くなれよ！', 
    command=lambda:syuzoGo(0))
    self.Button1.place(x=20,y=20)        


def main():
  root = tk.Tk()
  app = Application(master = root)
  app.mainloop()

if __name__ == "__main__":
  main()    