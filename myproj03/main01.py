"""
퀴즈) 코드 완성하기

* 1이상 40이하 범위에서 랜덤수를 획득하고
* 10 미만이라면 1을 출력하고'
* 10 이상 20 미만이라면 10을 출력하고
* 20 이상 30 미만이라면 20을 출력하고
* 30 이상이라면, "너무 큰 수" 라고 출력합니다.
* 프로그램 종료 시에 "숫자는 ???입니다." 라고 출력

"""
from random import randint

num = randint(1, 40)

if num < 10:
    print(1)
elif num < 20:
    print(10)
elif num < 30:
    print(20)
else:
    print("너무 큰 수")

print(f"숫자는 {num}입니다.")
