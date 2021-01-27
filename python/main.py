import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("x, y 함수") #제목
window.geometry("340x340") #가로 * 세로 사이즈

# x
x_lbl = Label(window, text = "x :")
x_lbl.place(x = 50, y = 50)
x = Entry(window, width = 20)
x.place(x = 70, y = 50)

# y
y_lbl = Label(window, text = "y :")
y_lbl.place(x = 50, y = 100)
y = Entry(window, width = 20)
y.place(x = 70, y = 100)

# 계산하는 함수
def func(event):
  result = int(tk.Entry.get(x)) + int(tk.Entry.get(y)) # x+ y로 출력
  res.delete(0, tk.END)
  res.insert(0, result)


# 계산 버튼
btn = ttk.Button(window, text='결과')
btn.place(x = 120, y = 150)
btn.bind('<Button-1>', func)

# 결과
res_lbl = Label(window, text = "결과 :")
res_lbl.place(x = 50, y = 200)
res = Entry(window, width = 15)
res.place(x = 90, y = 200)




window.mainloop()