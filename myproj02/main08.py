def cal_sum(max_num):
    accmulator = 0  # 누적할 변수
    for i in range(1, max_num + 1):
        accmulator += i
    return accmulator


print(cal_sum(100))
