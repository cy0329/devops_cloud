from tkinter import *
from tkinter import messagebox
# 버튼을 사용하여 알림 창 띄우기
def clickButton1() :
    messagebox.showinfo('내 위장 :', '역시 넌 내 주인이야!') # messagebox 타이틀, messagebox 내용
def clickButton2() :
    messagebox.showinfo('내 위장 :', '지x하고 자빠졌네')

window = Tk()
window.title("내 위장 :")
window.geometry('250x150')
label1 = Label(window, text='야 배 안고프냐?')
button1 = Button(window, text='항상 고프지', fg='red', command=clickButton1)
button2 = Button(window, text='아니 괜찮아', fg='blue', command=clickButton2)

label1.pack(pady=10)
button1.pack(side=LEFT, padx=10, pady=20) # expand >> 요구되지 않은 공간 사용하기
button2.pack(side=RIGHT, padx=10, pady=20)
window.mainloop()
