import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("정화통 사용시간 예측 프로그램") #제목
window.geometry("400x500") #가로 * 세로 사이즈

# title
title = Label(window, text = "정화통 사용시간 예측 프로그램 Ver 0.1", font=('Apple Gothic', 20))
title.place(y = 20)
title.pack()

x_lbl = Label(window, text = "x :")
x_lbl.place(x = 50, y = 50) #x라벨 배치
x = Entry(window, width = 20)
#x.place(x = 70, y = 50) #x엔트리 배치
x.pack()

# y
y_lbl = Label(window, text = "y :")
y_lbl.place(x = 50, y = 100) #y라벨 배치
y = Entry(window, width = 20)
y.place(x = 70, y = 100) #y엔트리 배치 

# 계산하는 함수
def func(event):
  result = int(tk.Entry.get(x)) + int(tk.Entry.get(y)) # x+ y 계산식
  res.delete(0, tk.END) #결과 엔트리 초기화
  res.insert(0, result) #결과 엔트리에 값 대입


# 계산 버튼
btn = ttk.Button(window, text='결과')
btn.place(x = 120, y = 150) #결과 버튼 배치
btn.bind('<Button-1>', func) #결과 버튼에 계산 함수 bind 

# 결과
res_lbl = Label(window, text = "결과 :")
res_lbl.place(x = 50, y = 200)
res = Entry(window, width = 17)
res.place(x = 90, y = 200)

window.mainloop() #window실행