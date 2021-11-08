def get_max_num(num_list):
    num = num_list[0]  # index 참조 - num_list에서 0번째를 먼저 num에 넣고 시작
    for current_num in num_list:
        if current_num > num:
            num = current_num
    return num


nums = [17, 92, 18, 33, 58, 7, 33, 42]
print(get_max_num(nums))  # 92를 기대중


def get_max_index(num_list):
    num = num_list[0]  # index 참조
    index = 0
    max_index = 0
    for current_num in num_list:
        if current_num > num:
            num = current_num
            max_index = index
        index += 1
    return max_index


nums = [17, 92, 18, 33, 58, 7, 33, 42]
print(get_max_num(nums))  # 92를 기대중
print(get_max_index(nums))  # 92가 몇번째인지 = 0을 기대중


def get_max_index(num_list):
    num = num_list[0]  # index 참조
    max_index = 0
    for index, current_num in enumerate(num_list):
        if current_num > num:
            num = current_num
            max_index = index
    return max_index


nums = [17, 92, 18, 33, 58, 7, 33, 42]
print(get_max_num(nums))  # 92를 기대중
print(get_max_index(nums))  # 92가 몇번째인지 = 0을 기대중

# max(nums) 해버리면 사실 위 과정과 같음  >> 92 출력됨
