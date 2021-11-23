import pymysql

conn, cur = None, None # 따로 한줄씩 해줘도 됨

# 데이터베이스 접속
conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='sqldb', charset='utf8')

# 커서
cur = conn.cursor()
# 여기까지 실행해 봤을 때 아무일도 안 일어나야 잘 된 것

# userTBL의 회원 데이터 INSERT
sql = ''
# userID, name, birthYear, addr
userID = ''
name = ''
birthYear = ''
addr = ''

while True:
    userID = input("사용자 ID : ")
    if userID == '' :
        break
    name = input('사용자 이름 : ')
    birthYear = input('사용자 출생년도 : ')
    addr = input('사용자 주소 : ')

    sql = 'INSERT INTO userTBL (userID, name, birthYear, addr, mDate) VALUES '\
          "('"+userID+"', '"+name+"', "+birthYear+", '"+addr+"', CURDATE())"
    cur.execute(sql)

conn.commit()
conn.close()