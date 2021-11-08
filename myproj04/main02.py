for num in [3, 6, 9]:  # 1103과제 1에서 이렇게도 가능
    for i in range(1, 10):
        print(f"{num}*{i}={num*i}")

for i in range(1, 100):
    if i % 15 == 0:  # 1103과제 2에서 이렇게도 가능
        print(i)

# if i % (3*5) == 0 이렇게 해도 3,5의 공배수라는 것을
# 명시할 수 있음

acc = 0
for i in range(1, 100):
    if i % 15 == 0:  # 1103과제 3에서 이렇게도 가능
        acc += i
print(acc)

num_list = []
for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        num_list.append(i)  # 1103과제 3에서 이렇게도 가능
print(sum(num_list))


for number in range(2, 10):
    for i in range(1, number + 1):  # 1103과제 4에서 이렇게도 가능
        print(f"{number} * {i} = {number * i}")
