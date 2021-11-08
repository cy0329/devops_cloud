# 1104 과제 다시 확인
# 오전 수업에서 추가된 내용들 확인 꼭 하고 공부

from collections import Counter
import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())
print(song_list)

"""
방탄소년단의 곡명만 출력해보세요.
"""

for song_dict in song_list:
    if song_dict["artist"] == "방탄소년단":
        print(song_dict["title"])

"""
제목에 '가을'이 들어간 곡 출력
"""
for song_dict in song_list:
    if "가을" in song_dict["title"]:
        print(song_dict["title"])

"""
좋아요 수 20만 넘는 곡 수 출력
"""

song_count = 0
for song_dict in song_list:
    if song_dict["like"] > 200_000:
        song_count += 1
print(f"좋아요가 20만이 넘는 곡은 {song_count}곡입니다.")

"""
가수 별 곡 수 출력
"""
# 여기 집중

artist_dict = {}
# artist_list = []
for song_dict in song_list:
    artist: str = song_dict["artist"]  # 타입힌트로 artist가 문자열임을 미리 명시
    if artist not in artist_dict:
        artist_dict[artist] = 0
    artist_dict[artist] += 1

    # artist_list.append(artist)
print(artist_dict)

{  # 사전 자료구조
    #   key     :  value
    "방탄소년단": 10,
}

"""
Counter 사용해서 하는 방식
"""

# artist_list = []
# for song_dict in song_list:
##    artist: str = song_dict["artist"] # << 이부분은 없어도 됨
#     artist_list.append(song_dict['artist'])

# List Comprehension 위 주석 코드와 아래 코드는 같다.
artist_list = []
artist_list = [song_dict["artist"] for song_dict in song_list]


print(Counter(artist_list))

# fmt: on
counter = Counter(artist_list)
# for artist in counter: #keys
#     print(artist)

# for song_count in counter.values():  # values
#     print(song_count)

# for artist in counter:
#     print(artist, counter[artist])  # 이 방식은 잘 안씀

for artist, song_counter in counter.items()  # .items << 키와 값을 한번에 가져온다
    print(artist, song_count)