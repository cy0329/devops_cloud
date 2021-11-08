"""
map 부분까지 과제
"""

import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())
# print(song_list)

"""
과제#1. 멜론TOP100 리스트에서 '곡명'의 '단어 수' 출력
hint : 총 100줄 중에 한 줄 출력의 예 :Dynamite => 1
"""
## 방식1
# 1. 일단 필터나 맵 등을 사용하지 않고 코드를 짜본다.
# 2. 짠 코드에서 변환함수를 정의할 부분을 선택해본다.
# 3. map(변환함수, iterable) 형식으로 만들어 대입해본다
# for s['title'] in song_list:


## 방식2
# 1. 곡명의 단어수를 뽑는 함수 정의
# 2.


def map_fn1(song_dict):
    ch = len(song_dict["title"].split())
    return ch


print(map(map_fn1(song_list), song_))

"""
과제#2. 멜론TOP100 리스트에서 'top10' '곡명' 출력 
hint : 단어 수가 제일 큰 노래가 우선순위가 가장 높다. (sort 활용하면 될듯)
"""
