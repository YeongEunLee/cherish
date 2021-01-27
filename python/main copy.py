import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("x, y 함수") #제목
window.geometry("340x340") #가로 * 세로 사이즈

# x
x_lbl = Label(window, text = "x :")
x_lbl.place(x = 50, y = 50)
x_txt = Entry(window, width = 20)
x_txt.place(x = 70, y = 50)

# y
y_lbl = Label(window, text = "y :")
y_lbl.place(x = 50, y = 100)
y_txt = Entry(window, width = 20)
y_txt.place(x = 70, y = 100)

# 계산 버튼
xy_button = ttk.Button(window, text='결과')
xy_button.place(x = 120, y = 150)

# 결과
#res_lbl = Label(window, text = "결과 :")
#res_lbl.place(x = 50, y = 200)
#res_txt = Entry(window, width = 30)



window.mainloop()