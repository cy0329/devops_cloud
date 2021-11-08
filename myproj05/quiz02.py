"""
멜론Top100 리스트에서 '좋아요' Top10 곡명 출력
"""
import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


# sorted(song_dict, key=aaa) 이 형식 사용

song_count = 0
for song_dict in song_list:
    sorted(song_dict['like'], reverse = True, key= )
