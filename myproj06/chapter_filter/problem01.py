from typing import List
import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())
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
for song_dict in new_song_list:
    print("{title} / {value}".format(**song_dict))
