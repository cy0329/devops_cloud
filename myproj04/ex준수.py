# 문자열을 인자로 받아, 단어수를 반환하는 함수
def get_word_count(s):
    return len(s.split(" "))


sentence = input("문장을 입력하세요 : ")
print(get_word_count(sentence))


# 문자열을 인자로 받아 공백을 제외한 글자를 반환하는 함수
# acc = [] 여기에 썼는데 이걸 def 안에 넣어야 함.
# 안그럼 10씩 계속 누적 >> 전역변수 (global variable)
# 전역변수는 거의 쓰지 않는다.
def get_count(s):
    acc = []  # 여기에 써주어야 한번 함수 사용 후 acc가 사라짐 >>
    # 지역변수 ()
    for i in s:
        if i != " ":
            acc.append(i)
    return len(acc)


sentence = "우리는 파이썬을 즐겨요"
print(get_count(sentence))

# 자연수를 인자로 받아, 천 단위 절사한 값을 리턴하는 함수
def send_1000(s):
    div = s // 1000
    multi = div * 1000
    return multi


number = int(input(" 숫자를 입력하세요"))
print(send_1000(number))
