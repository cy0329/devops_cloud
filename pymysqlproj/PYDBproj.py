import pymysql
from tkinter import *
from tkinter import messagebox

# 데이터베이스 연동 함수
def insertData(): # 입력부분에서는 EXCEPT 부분이 필수적(오류가 나기 때문에)
    conn, cur = None, None
    conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='sqldb', charset='utf8')
    cur = conn.cursor()

    # 회원 정보 insert 기능 구현
    # 사용자에게 입력받은 회원 정보 초기화
    userID, name, birthYear, addr = '','','',''
    # GUI에서 입력한 데이터 담기
    userID = edt1.get()
    name = edt2.get()
    birthYear = edt3.get()
    addr = edt4.get()

    # sql 쿼리 만들기
    sql = ""
    sql = 'INSERT INTO userTBL (userID, name, birthYear, addr, mDate) VALUES '\
          "('"+userID+"', '"+name+"', "+birthYear+", '"+addr+"', CURDATE())"
    print(sql)
    # 쿼리 실행
    try :
        cur.execute(sql)
    except: # 예외처리 - 잘 맞게 정보를 입력해도 문제가 날 경우 >> 이렇게 해주어야 프로그램이 죽지 않고 그대로 흘러감
        messagebox.showerror("입력오류", "데이터 입력 오류가 발생 했습니다.")
    else:
        # 쿼리 실행이 오류없이 완료
        # 1) 메시지 박스로 성공 알림
        messagebox.showinfo("성공","회원 정보가 등록되었습니다.")
        # 2) 데이터 커밋(실제 저장)
        conn.commit()
        # 3) 테이블 조회(새로고침)
        selectData()

    # GUI에 입력한 데이터 삭제
    edt1.delete(0, "end")
    edt2.delete(0, "end")
    edt3.delete(0, "end")
    edt4.delete(0, "end")

    conn.close()



def selectData():
    conn, cur = None, None

    lUserID, lName, lBirthYear, lAddr = [], [], [], []

    conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='sqldb', charset='utf8')
    cur = conn.cursor()

    # 데이터 초기화
    lUserID.append('회원 ID')
    lUserID.append('-----------')

    lName.append('회원명')
    lName.append('-----------')

    lBirthYear.append('출생년도')
    lBirthYear.append('-----------')

    lAddr.append('주소')
    lAddr.append('-----------')

    # select 기능 구현
    sql = "SELECT userID, Name, birthYear, addr FROM userTBL ORDER BY mDate DESC"
    cur.execute(sql)


    while True:
        row = cur.fetchone()
        if row == None:
             break
        lUserID.append(row[0])
        lName.append(row[1])
        lBirthYear.append(row[2])
        lAddr.append(row[3])

    # GUI ListBox에 insert
    # listUserID, listName, listBirthYear, listAddr
    # 1) 리스트 박스 초기화
    listUserID.delete(0,listUserID.size() - 1)
    listName.delete(0, listName.size() - 1)
    listBirthYear.delete(0, listBirthYear.size() - 1)
    listAddr.delete(0, listAddr.size() - 1)

    # 2) select 해온 데이터 insert
    for item1, item2, item3, item4 in zip(lUserID, lName, lBirthYear, lAddr):
        listUserID.insert(END, item1)
        listName.insert(END, item2)
        listBirthYear.insert(END, item3)
        listAddr.insert(END, item4)


# GUI 화면 구성
window = Tk()
window.geometry('800x300')
window.title('MariaDB 연동 GUI')

editFrame = Frame(window)
editFrame.pack()

listFrame = Frame(window)
listFrame.pack(side=BOTTOM, fill=BOTH, expand=1)

label1 = Label(editFrame, text='회원 ID')
label1.pack(side=LEFT, padx=10, pady=10)

edt1 = Entry(editFrame, width=10)
edt1.pack(side=LEFT, padx=10, pady=10)

label2 = Label(editFrame, text='회원명')
label2.pack(side=LEFT, padx=10, pady=10)

edt2 = Entry(editFrame, width=10)
edt2.pack(side=LEFT, padx=10, pady=10)

label3 = Label(editFrame, text='출생년도')
label3.pack(side=LEFT, padx=10, pady=10)

edt3 = Entry(editFrame, width=10)
edt3.pack(side=LEFT, padx=10, pady=10)

label4 = Label(editFrame, text='회원 주소')
label4.pack(side=LEFT, padx=10, pady=10)

edt4 = Entry(editFrame, width=10)
edt4.pack(side=LEFT, padx=10, pady=10)

# 버튼
btnInsert = Button(editFrame, text='입력', command=insertData)
btnInsert.pack(side=LEFT, padx=10, pady=10)

btnInsert = Button(editFrame, text='조회', command=selectData)
btnInsert.pack(side=LEFT, padx=10, pady=10)

# 리스트
listUserID = Listbox(listFrame)
listUserID.pack(side=LEFT, fill=BOTH, expand=1)

listName = Listbox(listFrame)
listName.pack(side=LEFT, fill=BOTH, expand=1)

listBirthYear = Listbox(listFrame)
listBirthYear.pack(side=LEFT, fill=BOTH, expand=1)

listAddr = Listbox(listFrame)
listAddr.pack(side=LEFT, fill=BOTH, expand=1)

window.mainloop()