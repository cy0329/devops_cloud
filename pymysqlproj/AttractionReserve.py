import pymysql
from tkinter import *
from tkinter import messagebox

def searchatt():
    conn, cur = None, None
    latts, lendtime = [], []
    conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='cydb', charset='utf8')
    cur = conn.cursor()
    # 첫줄 디폴트 값 주기
    latts.append('번호--어트랙션')
    latts.append('-----------------------------------')
    lendtime.append('이용 마감 시간')
    lendtime.append('-----------------------------------')

    sql = "SELECT AttNo, AttName, EndTime FROM attractions"
    cur.execute(sql)

    while True:
        row = cur.fetchone()
        if row == None:
             break
        ANo = str(row[0])
        ANm = row[1]
        AEt = str(row[2])
        latts.append(ANo+"--"+ANm.ljust(30))
        lendtime.append(AEt+'시')

    # GUI ListBox에 insert
    # 1) 리스트 박스 초기화
    listAtt.delete(0, listAtt.size() - 1)
    listEndtime.delete(0, listEndtime.size() - 1)
    # 2) select 해온 데이터 insert
    for item1, item2 in zip(latts, lendtime):
        listAtt.insert(END, item1)
        listEndtime.insert(END, item2)


# 새 창 띄워서 결과 보여주기
def newwindow():
    global newwindow
    newwindow = Toplevel()

    newwindow.title('예약 정보')
    newwindow.geometry('300x250+900+100')
    # 프레임 세팅
    NeditFrame = Frame(newwindow)
    NeditFrame.pack()

    NlistFrame = Frame(newwindow)
    NlistFrame.pack()

    # 결과 도출 박스
    Nlabel1 = Label(NeditFrame, text='예약 정보')
    Nlabel1.pack(side=TOP, pady=10)

    Nlistuserres = Listbox(NlistFrame)
    Nlistuserres.pack(side=TOP, fill=BOTH, expand=1)

    # 리셋 버튼으로 저장된 예약 정보 삭제하기
    def resetbtn():
        conn, cur = None, None
        conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='cydb', charset='utf8')
        cur = conn.cursor()

        reset_sql = 'DELETE FROM attres'
        try:
            cur.execute(reset_sql)
        except:
            messagebox.showerror("초기화 오류", "초기화가 제대로 실행되지 않았습니다.")
        else:
            messagebox.showinfo("초기화 완료", "예약 정보가 초기화되었습니다.\n창을 닫고 다시 입력해주세요.")
        conn.commit()
        Nlistuserres.delete(0, Nlistuserres.size() - 1)
        Nlistuserres.insert(END, '예약자명-예약')
        Nlistuserres.insert(END, '----------------')


    Nbtnreset = Button(NlistFrame, text='예약정보 초기화', command=resetbtn)
    Nbtnreset.pack(side=BOTTOM, padx=10, pady=10)

    # 새 창에서 보여줄 것
    conn, cur = None, None

    luserres = []

    conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='cydb', charset='utf8')
    conn.commit()
    cur = conn.cursor()

    # 데이터 초기화
    luserres.append('예약자명-예약')
    luserres.append('----------------')

    # select 기능 구현
    sql = "SELECT R.userName, A.AttName  " \
          "FROM attractions A	" \
          "INNER JOIN attres R	" \
          "ON A.AttNo = R.res1 OR A.AttNo = R.res2 " \
          "OR A.AttNo = R.res3 OR A.AttNo = R.res4 " \
          "OR A.AttNo = R.res5	" \
          "GROUP BY R.userName, A.AttNo"
    cur.execute(sql)

    while True:
        row = cur.fetchone()
        if row == None:
            break
        luserres.append(row[0]+' - '+row[1])


    # GUI ListBox에 insert
    # listUserID, listName, listBirthYear, listAddr
    # 1) 리스트 박스 초기화
    Nlistuserres.delete(0, Nlistuserres.size() - 1)

    # 2) select 해온 데이터 insert
    for item1 in luserres:
        Nlistuserres.insert(END, item1)

    conn.close()



def insertData():  # 입력부분에서는 EXCEPT 부분이 필수적(오류가 나기 때문에)
    conn, cur = None, None
    conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='cydb', charset='utf8')
    cur = conn.cursor()

    # 사용자에게 입력받은 회원 정보 초기화
    userName, res1, res2, res3, res4, res5 = '', '', '', '', '', ''
    # GUI에서 입력한 데이터 담기
    userName = edt1.get()
    res1 = edt2.get()
    res2 = edt3.get()
    res3 = edt4.get()
    res4 = edt5.get()
    res5 = edt6.get()

    # sql 쿼리 만들기
    sql = ""
    sql = 'INSERT INTO attres (userName, res1, res2, res3, res4, res5) VALUES ' \
          "('"+userName+"', "+res1+", "+res2+", "+res3+", "+res4+", "+res5+")"
    # 쿼리 실행
    try:
        cur.execute(sql)
    except:  # 예외처리 - 잘 맞게 정보를 입력해도 문제가 날 경우 >> 이렇게 해주어야 프로그램이 죽지 않고 그대로 흘러감
        messagebox.showerror("입력오류", "데이터 입력 오류가 발생 했습니다.")
    else:
        # 쿼리 실행이 오류없이 완료
        # 1) 메시지 박스로 성공 알림
        messagebox.showinfo("성공", "예약 정보가 등록되었습니다.")
        # 2) 데이터 커밋(실제 저장)
        conn.commit()
        # 3) 테이블 조회(새로고침)


    # GUI에 입력한 데이터 삭제
    edt1.delete(0, "end")
    edt2.delete(0, "end")
    edt3.delete(0, "end")
    edt4.delete(0, "end")
    edt5.delete(0, "end")
    edt6.delete(0, "end")

    conn.close()





# GUI 화면 구성
window = Tk()
window.title('애버랜드 어트랙션 예약')
window.geometry('500x500+400+100')
window.resizable(False, False)

# frame 설정
editFrame = Frame(window)
editFrame.pack(side=TOP)

editFrame1 = Frame(window)
editFrame1.pack(side=RIGHT)

editFrame2 = Frame(window)
editFrame2.pack(side=LEFT)

listFrame = Frame(window)
listFrame.pack(side=BOTTOM, fill=BOTH, expand=1)

#나머지 GUI 위치 설정
label = Label(editFrame, text='★에버랜드에 오신걸 환영합니다★')
label.pack()

btnInsert = Button(editFrame2, text='어트랙션 조회', command=searchatt)
btnInsert.pack(padx=4, pady=4)

label0 = Label(editFrame1, text='예약할 어트랙션의 \n"번호"\n를 입력해주세요', relief=SOLID)
label0.pack(side=TOP, padx=10, pady=4)

label1 = Label(editFrame1, text='이름')
label1.pack(side=TOP, padx=10, pady=4)

edt1 = Entry(editFrame1, width=10)
edt1.pack(side=TOP, padx=10, pady=4)

label2 = Label(editFrame1, text='어트랙션1')
label2.pack(side=TOP, padx=10, pady=4)

edt2 = Entry(editFrame1, width=10)
edt2.pack(side=TOP, padx=10, pady=4)

label3 = Label(editFrame1, text='어트랙션2')
label3.pack(side=TOP, padx=10, pady=4)

edt3 = Entry(editFrame1, width=10)
edt3.pack(side=TOP, padx=10, pady=4)

label4 = Label(editFrame1, text='어트랙션3')
label4.pack(side=TOP, padx=10, pady=4)

edt4 = Entry(editFrame1, width=10)
edt4.pack(side=TOP, padx=10, pady=4)

label5 = Label(editFrame1, text='어트랙션4')
label5.pack(side=TOP, padx=10, pady=4)

edt5 = Entry(editFrame1, width=10)
edt5.pack(side=TOP, padx=10, pady=4)

label6 = Label(editFrame1, text='어트랙션5')
label6.pack(side=TOP, padx=10, pady=4)

edt6 = Entry(editFrame1, width=10)
edt6.pack(side=TOP, padx=10, pady=4)
# 버튼
btnInsert = Button(editFrame1, text='입력', command=insertData)
btnInsert.pack(fill='x', padx=10, pady=4)

btnInsert = Button(editFrame1, text='조회', command=newwindow)
btnInsert.pack(fill='x', padx=10, pady=4)

# 리스트
listAtt = Listbox(listFrame)
listAtt.pack(side=LEFT, fill=BOTH, expand=1)

listEndtime = Listbox(listFrame)
listEndtime.pack(side=LEFT, fill=BOTH, expand=1)

window.mainloop()