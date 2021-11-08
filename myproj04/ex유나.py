#1. 문자열을 인수로 받아 단어 수를 반환하는 함수
def get_word_count(s):
    s.split()
    return len(s)

#2. 문자열을 인자로 받아 공백을 제외한 글자수를 반환하는 함수 
def get_word_count_split(word):
    word_split = word.split(" ")
    return len(word_split)
get_word_count_split("우리는 파이썬을 즐겨요")
    
#3. 자연수를 인자로 받아 절사값 리턴
def number_return(number):
    input_number = 0
    input_number = (number // 1000) *1000
    return input_number
number_return(1234567)