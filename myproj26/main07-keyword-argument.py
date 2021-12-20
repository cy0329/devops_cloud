def mysum3(x, y, z):
    return x + y * 10 + z * 100


# Positional Argument (순서가 중요)
print(mysum3(1, 2, 3))

# Keyword Argument
print(mysum3(x=1, y=2, z=3))
# 순서가 바뀌어도 상관x
print(mysum3(z=3, x=1, y=2))

kwargs = {"x": 1, "y": 2, "z": 3}
mysum3(**kwargs)  # unpacking


# ...

people = [
    {"name": "Tom", "age": 10, "region": "Seoul"},
    {"name": "Steve", "age": 12, "region": "Pusan"},
]

for person in people:
    print(person["name"], person["age"])
