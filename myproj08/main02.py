from typing import List
import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


"""
멜론TOP100 리스트에서 "곡명 / 단어수"의 리스트를 만들어봅시다.
총 100줄 중에 한 줄 출력 의 예 : Dynamite ➡ 1
"""

# for song_dict in song_list:
#     title: str = song_dict['title']
#     title_length = len(title)
#     title, title_length
#     print(title, title_length)


# def get_title_for_song(song_dict):
#     return song_dict["title"]


# for song_dict in song_list:
#     # 변환을 담담하는 함수  >> 필터는 통과 시키냐 마냐
#     print(get_title_for_song(song_dict))

# title_list = list(map(get_title_for_song, song_list))
# print(title_list)

# for song_dict in filter(함수, song_list):

# for title in map(get_title_for_song, song_list):
#     print(f"{title} - {len(title)}")


# def get_title_and_length_for_song(song_dict):
#     title: str = song_dict["title"]
#     return [title, len(title)]


# for title, length in map(get_title_and_length_for_song, song_list):
#     print(title, "=>", length)

# 방탄소년단의 노래에 대해서만, 곡명과 곡명의 글자수를 출력

# bts_list = []
# for song_dict in song_list:
#     if song_dict["atrist"] == "방탄소년단":
#         title: str = song_dict["title"]
#         bts_list.append([title, len(title)])

# for title, length in bts_list:
#     print(title, length)

# filter/map 버전
# def check_bts_song(song_dict):
#     return song_dict["artist"] == "방탄소년단"


# for title, length in map(
#     get_title_and_length_for_song, filter(check_bts_song, song_list)
# ):
#     print(title, length)

# 문제
# artist 글자수가 3글자 이상인 곡에 대해
# 좋아요 수와 제목글자수의 곱을 출력

# 1) for/if 로 구현
new_song_list: List[dict] = []
for song_dict in song_list:
    if len(song_dict["artist"]) >= 3:
        value: int = song_dict["like"] * len(song_dict["title"])
        new_song_list.append(dict(song_dict, value=value))
        # new_song_list.append(  # 위 한줄짜리와 같음
        #     {
        #         "title": song_dict["title"],
        #         "artist": song_dict["artist"],
        #         "like": song_dict["like"],
        #         "album": song_dict["album"],
        #         "rank": song_dict["rank"],
        #         "value": value,
        #     }
        # )

print("=========================")

# 2) filter/map 위주로 구현
def fil_ov_three_let(song_dict):
    return len(song_dict["artist"]) >= 3


def map_mul_like_and_length(song_dict):
    return song_dict["like"] * len(song_dict["title"])


answer = list(map(map_mul_like_and_length, filter(fil_ov_three_let, song_list)))
print(answer)


"""
멜론TOP100 리스트에서 "곡명" 단어수로 TOP10 곡명 출력
단어수가 제일 큰 노래가 우선순위가 가장 높겠죠.
"""
