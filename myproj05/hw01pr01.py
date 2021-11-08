"""
첫 과제 확인하기 (랜덤 숫자 맞추기)
"""

from random import randint

number = randint(1, 100)
# is_pass = False  # Flag 변수
for retry in range(1, 11):
    line = input(f"[{retry}]Try guess number : ")
    try:
        answer = int(line.strip())
    except ValueError:
        print("잘못된 값을 입력하였습니다.")
        continue

    # answer = int(line.strip() or 0)  # a or b << a 가 거짓일때 b를 사용한다.

    if answer == number:
        print(f"{retry}회 시도에 성공")
        # is_pass = True
        break  # break에 가장 가까이 있는 루프(for)만 빠져나옴
    elif answer < number:
        print("더 큰수를 입력해주세요.")
        pass
    elif answer > number:  # else:
        print("더 작은 수를 입력해주세요.")
        pass
else:  # for에서 모든 회차를 다 시도했다 하면 else로 나옴
    print("다음 기회에...")
