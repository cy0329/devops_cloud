from tkinter import *
from tkinter import messagebox
# 버튼을 사용하여 알림 창 띄우기
def clickButton() :
    messagebox.showinfo('버튼 클릭', '버튼을 클릭했습니다.') # messagebox 타이틀,
                                                        # messagebox 내용

window = Tk()
window.title("버튼 이벤트 연습")
window.geometry('400x400')
button1 = Button(window, text='버튼1', command=clickButton)
button2 = Button(window, text='버튼2', command=clickButton)
button3 = Button(window, text='버튼3', command=clickButton)

button1.pack(side=TOP, padx=10, pady=10)
button2.pack(side=TOP, padx=10, pady=10)
button3.pack(side=TOP, padx=10, pady=10)

window.mainloop()
