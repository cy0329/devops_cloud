"""
1. 반복문을 활용하여, 효과적으로 3,6,9단 구구단 출력하기
"""

for num in range(3, 10, 3):
    print(f"<<{num}단>>")
    for i in range(1, 10):
        print(f"{num}*{i}={num*i}")
