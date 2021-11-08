# 기초 데이터로서 멜론 top100 리스트 구성하기

import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

print("====== 과제 1 ======")

for s in song_list:
    if s["artist"] == "방탄소년단":
        print(s["title"])

print("====== 과제 2 ======")

for t in song_list:
    if "가을" in t["title"]:
        print(t["title"])

print("====== 과제 3 ======")

num_of_song = 0
for l in song_list:
    if l["like"] >= 200000:
        num_of_song += 1
print("좋아요가 20만이 넘는 곡의 수 : ", num_of_song)

print("====== 과제 4 ======")

중복가수 = []
for n1 in song_list:
    중복가수.append(n1["artist"])

가수 = set(중복가수)


for n2 in 가수:
    count = 0
    for n3 in 중복가수:
        if n2 == n1:
            count += 1
    print(가수, "의 곡 수 : ", count)
