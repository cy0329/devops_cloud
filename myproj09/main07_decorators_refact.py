"""가독성 좋게 장식자 사용해서 써보기"""

import time

# 인자에 대한 리턴값을 저장
# - key : 인자 값에 대한 튜플
# - value : 그 인자로 함수를 수행했을 때의 리턴값


# cached = {}  # 전역변수 (가급적 지양해야함.) 딕셔너리 선언

# def mysum2(x, y):
#     key = (x, y)
#     if key not in cached:  # key 로서 계산된 적이 없다면
#         time.sleep(1)  #  1초간 대기
#         cached[key] = x + y + 10
#     return cached[key]

# cached2 = {}

# def mymultiply2(x, y):
#     key = (x, y)
#     if key not in cached2:
#         time.sleep(1)
#         cached2[key] = x * y + 10
#     return cached2[key]

# 장식자 구현의 가장 기초적인 방법
def memoize(fn):  # memoize 가 호출이 될 때마다 새로운 cached가 만들어짐
    cached = {}

    def wrap(x, y):
        key = (x, y)
        if key not in cached:
            cached[key] = fn(x, y)
        return cached[key]

    return wrap


# =========================================== #
@memoize  ### 이게 장식자!! 아래 # mysum2 =  이거 부분이 @memoize 로 그냥 끝
def mysum2(x, y):
    time.sleep(1)
    return x + y + 10


# mysum2 = memoize(mysum2)  ## 이 순간부터 mysum2는 위에 wrap이 됨


@memoize
def mymultiply2(x, y):
    time.sleep(1)
    return x * y + 10


# mymultiply2 = memoize(mymultiply2)

print(mysum2(1, 2))
print(mysum2(1, 3))
print(mysum2(1, 3))
print(mysum2(1, 2))
print(mysum2(1, 2))
print(mymultiply2(1, 2))
print(mymultiply2(1, 2))
print(mymultiply2(1, 3))
print(mymultiply2(1, 3))
