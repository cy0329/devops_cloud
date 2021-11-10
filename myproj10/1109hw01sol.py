def myfilter(filter_fn, alter_value):
    def wrap(fn):
        def inner(*args):
            # new_args = [filter_fn(i) and alter_value or args for i in args]
            # 아래 2줄은 위에 한줄로 가능  *List Comprehension
            # 이것도 아래와 같은 이유로 안됨
            new_args = []
            for i in args:
                # new_args.append(filter_fn(i) and alter_value or args)
                # 근데 이렇게 하면 alter_value가 0이라 bool판단에서 잘못되버림

                # 아래 4줄이 위에 한줄로 가능 (for문 안에 한줄)
                if filter_fn(i):
                    i = alter_value
                    new_args.append(i)
                else:
                    new_args.append(i)

            return fn(*new_args)

        return inner

    return wrap


@myfilter(lambda i: i % 2 == 0, 0)
def mysum(a, b, c, d, e):
    return a + b + c + d + e


@myfilter(lambda i: i % 2 == 0, 1)
def mymultiply(a, b, c, d, e):
    return a * b * c * d * e


print(mysum(1, 2, 3, 4, 5))  # 결과값 = 9
print(mymultiply(1, 2, 3, 4, 5))  # 결과값 = 15
