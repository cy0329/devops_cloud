"""
#1. 문자열을 인자로 받아, 단어수를 반환하는 함수를 작성
"""


def get_word_count(s):
    n = s.split(" ")
    return len(n)


n = input("단어 수를 세어보기 : ")
print(get_word_count(n))

"""
#2. 문자열을 인자로 받아, 공백을 제외한 글자를 반환하는 함수를 작성
"""


def get_ch_count_except_space(s):
    acc = []
    for ch in s:
        if ch != " ":
            acc.append(ch)
    return len(acc)


m = input("공백 제외 글자수 세보기 : ")
print(get_ch_count_except_space(m))

"""
#3. 자연수를 인자로 받아, 천단위 절사한 값을 리턴하는 함수를 작성
"""


def cut_th(s):
    return (s // 1000) * 1000


num = int(input("천단위 절사 : "))
print(cut_th(num))
