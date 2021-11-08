# 숫자 퀴즈
# 랜덤 숫자 맞추기

# hint : random.randint를 통해 1 이상 100 이하의 랜덤수를 만든다.

# 유저에게 10회의 기회를 준다. for와 range를 잘 써서만들어볼 수 있음
# 그 숫자를 정확히 맞췄다면, 몇 번 만에 맞췄는지 출력
# 입력한 숫자가 랜덤 수보다 작다면 '더 큰 수를 입력해주세요'라고 출력
# 입력한 숫자가 랜덤 수보다 크다면 '더 작은 수를 입력해주세요'라고 출력
# 횟수를 초과했다면, '다음 기회에...'라고 출력

import random

x = random.randint(1, 100)

for i in range(10):
    print(f"남은 기회:{10-i}회")
    answer = input("1~100중에 숫자를 맞춰보세요. : ")
    a = int(answer)
    if i == 9:
        print("\n10회 끝 다음기회에..")
        break
    if a == x:
        print("정답!")
        break
    if a > x:
        print("\n더 작은 수를 입력해주세요.")
    if a < x:
        print("\n더 큰 수를 입력해주세요.")
