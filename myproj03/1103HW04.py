"""
4. 구구단 퀴즈 break 안쓴 버전
"""

for num in range(2, 10):
    print(f"### {num}단 ###")
    for i in range(1, 10):
        if i <= num:
            print(f"{num}*{i}={num*i}")
