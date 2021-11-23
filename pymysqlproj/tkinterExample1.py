from tkinter import *

# 문자를 표현할 수 있는 라벨 사용
window = Tk()
window.title("라벨 연습")
# window.geometry('400x100') # 가로 * 새로 사이즈, 지정 안해주면 딱맞게 나옴
# window.resizable(width=FALSE, height=TRUE) # 가로 새로 늘리기 가능/불가능 여부
# GUI 화면 코딩
label1 = Label(window, text='This is MariaDB를')
label2 = Label(window, text='열심히', font=('궁서체',26),
               fg='blue')
label3 = Label(window, text='공부 중입니다.',bg='magenta',
               width=20, height=5, anchor=SE)
        # 레이블이 올라갈 윈도우, 출력될 글
        # 설정: font, fg=폰트색, bg=배경색, anchor=글자의 위치
        # anchor의 디폴트는 center

# '위젯에 올려' 줘야함
label1.pack()
label2.pack()
label3.pack()

window.mainloop()
