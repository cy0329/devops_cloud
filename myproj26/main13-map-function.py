import random

numbers = [31, 89, 24, 81, 46]

# 31, 81, 24, 46, 89  # ASC (1의 자리 기준)
#  1   1   4   6   9
# 1) 내장함수 sorted
print(sorted(numbers))  # 오름차순 정렬
print(sorted(numbers, reverse=True))  # 내림차순 정렬


def make_value(number):
    return number % 10


print(sorted(numbers, key=make_value))

# 2) 리스트의 sort
# numbers.sort()
# numbers.sort(key=make_value)
# print(numbers)

# numbers.sort(key=lambda number: number % 10)
# print(numbers)


def make_random_value(number):
    return random.randint(1, 100)


numbers.sort(key=make_random_value)
print("random values :", numbers)

# -----

# # 내장함수 map
# # def mapper(number):
# #     return number ** 2
# # print(list(map(mapper, numbers)))

# print(list(map(
#     lambda number: number ** 2,
#     numbers,
# )))

# # new_numbers = []
# # for number in numbers:
# #     new_numbers.append(number ** 2)

# # # list comprehension
# # new_numbers = [
# #     number ** 2 for number in numbers
# # ]
