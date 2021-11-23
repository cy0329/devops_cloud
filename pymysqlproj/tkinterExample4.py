from tkinter import *
from tkinter import messagebox
# 버튼을 사용하여 알림 창 띄우기
def clickButton() :
    messagebox.showinfo('버튼 클릭', '버튼을 클릭했습니다.') # messagebox 타이틀,
                                                        # messagebox 내용

window = Tk()
window.title("입력관련 연습")
window.geometry('300x300')
# 프레임 = 영역 나누기
# 엔트리 = 입력 상자(사용자에게 입력 받는 상자, input())
# 리스트박스 = 목록(조회 결과 상자, 여러개의 row를 표현해야 할 때)

# 프레임으로 upFrame, downFrame으로 나눠서 영역을 사용
upFrame = Frame(window, relief='solid', bd=2)
upFrame.pack()

midFrame = Frame(window, relief='solid', bd=2)
midFrame.pack()

downFrame = Frame(window, relief='solid', bd=2)
downFrame.pack()

# 입력상자를 upFrame에 배치
editBox = Entry(upFrame, width=10)
editBox.pack(padx=20, pady=20)

button = Button(midFrame, text='중간')
button.pack(padx=20, pady=20)

# 리스트박스는 downFrame에 배치
listBox = Listbox(downFrame)
listBox.pack()

# 리스트박스에 값 입력
listBox.insert(END, '하나') # END는 위치
listBox.insert(END, '둘')
listBox.insert(END, '셋')

window.mainloop()
