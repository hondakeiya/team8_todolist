import sys
import tkinter

root = tkinter.Tk()
root.title(u"もっと...熱くなれよおおおおおおおおお")
root.geometry("400x300")

def DeleteEntryValue(event):
    #エントリーの中身を削除
    EditBox.delete(0, tkinter.END)

EditBox = tkinter.Entry(width=50)
EditBox.insert(tkinter.END,"てすと")
EditBox.pack()

EditBox.delete(0, tkinter.END)

value = EditBox.get()

Button = tkinter.Button(text=u'ボタンです')
Button.bind("<Button-1>",DeleteEntryValue) 
Button.pack()



root.mainloop()
