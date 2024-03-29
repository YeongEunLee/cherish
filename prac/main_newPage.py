try:
    import Tkinter as tk
except:
    import tkinter as tk
import tkinter as tk
import tkinter.ttk
from tkinter import *
from tkinter.ttk import *
import tkinter.font as tkFont

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Start page", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Go to page one",command=lambda: master.switch_frame(subPage)).pack()

class subPage(tk.Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.master = master
        self.master.title("정화통 사용시간 예측 프로그램")
        self.pack(fill=BOTH, expand=True)

        # 제목
        title = Frame(self)
        title.pack(fill=BOTH)

        fontStyle = tkFont.Font(family='Lucida Grande', size=20)

        label = Label(title, font = fontStyle, text = '정화통 사용시간 예측 프로그램 Ver.0.1')
        label.config(anchor=S)
        label.pack(fill=X, padx = 20 , pady = 20, expand=True)

        # 정화통 종류
        frame1 = Frame(self)
        frame1.pack(fill=X)

        lblCategory = Label(frame1, text="정화통 종류 : ", width=10)
        lblCategory.pack(side=LEFT, fill=X, padx=20, pady=10)

        # 정화통 종류 콤보박스
        values = ["직결식 소형"]
        comboCategory = tkinter.ttk.Combobox(frame1, values = values)
        comboCategory.pack(fill=X, padx = 20 , expand=True)

        # 가스종류
        frame2 = Frame(self)
        frame2.pack(fill=X)

        lblGas = Label(frame2, text="가스 종류 : ", width=10)
        lblGas.pack(side=LEFT, padx=20, pady=10)

        # 가스 종류 콤보박스
        values1 = ["cyclohexane"]
        comboGas = tkinter.ttk.Combobox(frame2, values = values1)
        comboGas.pack(fill=X, padx = 20 , expand=True)

        # 사용온도
        frame3 = Frame(self)
        frame3.pack(fill=X)

        lblT = Label(frame3, text="사용 온도 : ", width=10)
        lblT.pack(side=LEFT, padx=20, pady=10)

        entryT = Entry(frame3)
        entryT.pack(fill=X, pady=10, padx=20)

        # 사용 농도
        frame4 = Frame(self)
        frame4.pack(fill=X)

        lblC = Label(frame4, text="사용 농도 : ", width=10)
        lblC.pack(side=LEFT, padx=20, pady=10)

        entryC = Entry(frame4)
        entryC.pack(fill=X, pady=10, padx=20)

        # 사용 습도
        frame5 = Frame(self)
        frame5.pack(fill=X)

        lblH = Label(frame5, text="사용 습도 : ", width=10)
        lblH.pack(side=LEFT, padx=20, pady=10)

        entryH = Entry(frame5)
        entryH.pack(fill=X, pady=10, padx=20)
        
        # 계산하는 함수
        def func(event):
            result = 304.2 - 1.333*int(tk.Entry.get(entryT)) - 0.1369*int(tk.Entry.get(entryC)) + 0.00001868*int(tk.Entry.get(entryC))*int(tk.Entry.get(entryC))
            entryRes.delete(0, tk.END) #결과 엔트리 초기화
            entryRes.insert(0, result) #결과 엔트리에 값 대입

        # 사용시간 계산 버튼
        frame6 = Frame(self)
        frame6.pack(fill=X)
        btn = Button(frame6, text="사용시간계산 버튼")
        btn.pack(side=BOTTOM, padx=20, pady=10)
        btn.bind('<Button-1>', func)

        # 예상 사용 시간
        frame7 = Frame(self)
        frame7.pack(fill=X)

        lblRes = Label(frame7, text="예상사용시간 : ", width=10)
        lblRes.pack(side=LEFT, padx=20, pady=10)

        entryRes = Entry(frame7)
        entryRes.pack(fill=X, pady=10, padx=20)
    
        

def main():
    root = Tk()
    root.geometry("380x400+100+100")
    app = App()
    app.mainloop()

if __name__ == '__main__':
    main()
