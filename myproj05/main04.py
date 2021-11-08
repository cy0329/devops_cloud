# 순서 참조!! 이런 순서로 개발하면 개발이 수월하다!


def make_powered_list(numbers):
    new_numbers = []
    for number in numbers:
        new_numbers.append(number ** 2)
    return new_numbers


# map 방식


def make_powered_list2(numbers):
    make_power = lambda number: number ** 2
    return list(map(make_power, numbers))


# map은 리스트가 아니라 iterator로 반환..
