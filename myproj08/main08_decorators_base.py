def base(base_number):
    def wrap(fn):
        def inner(x, y):

            return fn(x, y) + base_number  # 여기서 fn이 아래 mysum2임

        return inner

    return wrap


base_10 = base(10)
base_20 = base(20)
base_100 = base(100)


# def base_10(fn):
#     def wrap(x, y):
#         return fn(x, y) + 10

#     return wrap


# def base_20(fn):
#     def wrap(x, y):
#         return fn(x, y) + 20

#     return wrap


@base(10)
@base(20)
@base(100)  # >> 인자를 갖는 장식자
def mysum2(x, y):
    return x + y


print(mysum2(1, 2))
