"""
2. 1 이상 100 미만 범위에서 3과 5의 공배수를 모두 출력하기
"""

for num in range(1, 100):
    if num % 3 == 0 and num % 5 == 0:
        print(num)
