def mysum2(x, y):
    return x + y + 10


def mysum3(x, y, z):
    return x + y + z + 10


# '가변인자' 문법
def mysum(x, y, *args):
    # *을 붙이면 0개 이상의 인자를 받음 앞에 x,y를 안써도 되는데 쓰면 인자를 최소 2개 이상은 받아야 한다는 것
    # 여러개 받으면 args 는 튜플로 받음
    print("args : ", args)
    return x + y + sum(args) + 10


print(mysum())
print(mysum(1))
print(mysum(1, 2))
print(mysum(1, 2, 3))
