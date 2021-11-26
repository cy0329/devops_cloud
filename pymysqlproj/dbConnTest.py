import pymysql

conn, cur = None, None # 따로 한줄씩 해줘도 됨

# 데이터베이스 접속
conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='sqldb', charset='utf8')

# 커서
cur = conn.cursor()
# 여기까지 실행해 봤을 때 아무일도 안 일어나야 잘 된 것

# userTBL의 회원 데이터 INSERT
sql = ''
# userID, name, birthYear, addr, mobile1, mobile2, height INSERT 시키도록
userID = ''
name = ''
birthYear = ''
addr = ''
mobile1 = ''
mobile2 = ''
height = ''


while True:
    userID = input("사용자 ID : ")
    if userID == '' :
        break
    name = input('사용자 이름 : ')
    birthYear = input('사용자 출생년도 : ')
    addr = input('사용자 주소 : ')
    mobile1 = input('사용자 전화번호 앞 3자리 : ')
    mobile2 = input('사용자 전화번호 뒤 8자리 : ')
    height = input('사용자 키 : ')

    sql = 'INSERT INTO userTBL (userID, name, birthYear, addr, mobile1, mobile2, height, mDate) VALUES '\
          "('"+userID+"', '"+name+"', "+birthYear+", '"+addr+"', '"+mobile1+"', '"+mobile2+"', "+height+", CURDATE())"
    # sql에서 쿼리문으로 들어갈 때 문자열은 무조건 작은 따옴표로 감싸져 있어야 하는 것이라서 문자열일땐 작은 따옴표로 감싸줌
    # "+여기 들어가는건 변수+" 변수를 "++"로 감싸줌으로써 변수의 값을 입력하는 것
    print(sql)
    cur.execute(sql)

conn.commit()
conn.close()