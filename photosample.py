import tkinter as tk

# rootメインウィンドウの設定
root = tk.Tk()
root.title("application")
root.geometry("250x150")

# メインフレームの作成と設置
frame = tk.Frame(root)
frame.pack(fill = tk.BOTH, padx=20,pady=10)


# 画像ファイルをインスタンス変数に代入
img = tk.PhotoImage(file="Syuzo.png")

big_img = img.zoom(2, 2)

button_big = tk.Button(frame, text="大画像", image=big_img, compound="top")

button_big.grid(row=0, column=2, padx=5)

root.mainloop()