s = "안녕하세요."

# # idx = 0
# # for ch in s:
# #     print(ch)
# #     idx += 1
# # 같은 동작 enumerate 가 index를 자동으로 뽑아줌
# 내가 원하는 번호로부터 1씩 증가하는 번호를 얻고자 > enumerate
# for idx, ch in enumerate(s, 1):
#     print(idx, ch)


mylist = [
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8],
    [9, 10],
]

for idx, (x, y) in enumerate(mylist):
    print(x, y)
