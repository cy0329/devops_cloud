# 띄어쓰기로 단어 구분하도록 할 수 있음
# ex) '우리는 파이썬을 즐겨요'를 인자로 받아, 3을 반환
# 힌트 '파이썬 자동화'.split()
def get_word_count(s):
    return s


# s 는 문자열


def get_ch_count_except_space(s):
    count = 0
    for ch in s:
        if ch != " ":
            count += 1
    return count


# s 는 문자열
# for ch in s:


def get_rounded_number(num):
    return (num // 1000) * 1000


print(get_rounded_number(45678))
# 1000으로 나눠서 몫만 취하는 방법
