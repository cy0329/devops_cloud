# sort 설명

import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


def 정렬기준값을_만들어줄_함수(song_dict):
    return song_dict["like"]


# 정렬을 하려면, 각 값들에 대한 대소비교가 가능해야한다.
# 10 < 100  '가' < '나'
# {'A': 1}  <  {"B": 2}  이렇게 비교가 안됨  *비교 기준이 있어야함

sorted_song_list = sorted(song_list, reverse=True, key=정렬기준값을_만들어줄_함수)

for song_dict in sorted_song_list[:10]:  # 여기서 [:10]이 10개까지만 정렬해줌. 리스트니까 슬라이싱 가능!!
    print("[{like}] {title} {artist}".format(**song_dict))

# for song_dict in sorted(song_list, reverse=True, key=정렬기준값을_만들어줄_함수):  # sorted를 통해 반환된건 무조건 list
#     print("[{like}] {title} {artist}".format(**song_dict))
# 이건 100개 전부를 정렬
