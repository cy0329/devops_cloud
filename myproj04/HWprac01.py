import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


중복가수 = []
for n1 in song_list:
    중복가수.append(n1["artist"])

가수 = set(중복가수)
# print(가수)


for n2 in 가수:
    count = 0
    for n3 in 중복가수:
        if n2 == n3:
            count += 1
    print(n2, "의 곡 수 : ", count)
