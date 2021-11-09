import time

# 인자에 대한 리턴값을 저장
# - key : 인자 값에 대한 튜플
# - value : 그 인자로 함수를 수행했을 때의 리턴값


cached = {}  # 전역변수 (가급적 지양해야함.) 딕셔너리 선언


def mysum2(x, y):
    key = (x, y)
    if key not in cached:  # key 로서 계산된 적이 없다면
        time.sleep(1)  #  1초간 대기
        cached[key] = x + y + 10
    return cached[key]


cached2 = {}


def mymultiply2(x, y):
    key = (x, y)
    if key not in cached2:
        time.sleep(1)
        cached2[key] = x * y + 10
    return cached2[key]


print(mysum2(1, 2))
print(mysum2(1, 3))
print(mysum2(1, 3))
print(mysum2(1, 2))
print(mysum2(1, 2))
print(mymultiply2(1, 2))
print(mymultiply2(1, 2))
print(mymultiply2(1, 3))
print(mymultiply2(1, 3))

# base_10이 호출될 때마다 새로운 함수 fn이 만들어짐
# def base(base_number):
#     def fn(x, y):
#         return x + y + base_number

#     return fn  # 함수로 함수를 만드는 것!


# base_10 = base(10) # 함수로 함수를 만드는 것!
# base_20 = base(20) # 함수로 함수를 만드는 것!
# print(base_10(1, 2))
# print(base_20(1, 2))


# name = "Tom"
# mysum = lambda x,y: x+y

# other_name = name
# other_fn = mysum

# def fn(x):
#     y = 'hello'
#     return y

# fn(name)
