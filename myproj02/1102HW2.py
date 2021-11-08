# 분당 타이핑 속도를 알려주도록 개선해보도록.
# 타자연습.PY에서 개선

import random
import time

animal_names = [
    "cat",
    "dog",
    "fox",
    "monkey",
    "mouse",
    "panda",
    "frog",
    "snake",
    "wolf",
]

input("준비 되셨으면 엔터를 눌러주세요.")

random.shuffle(animal_names)

begin_time = time.time()

ok_counter = 0

# for count in range(5):
# random_name = random.choice(animal_names)
# 방법1 : 이미 사용된 random_name을 받았다면
# 다시 가져오는 것
s = 0


for random_name in animal_names[0:5]:
    s += len(random_name)
    print(random_name)
    line = input(">>> ")
    if random_name == line:
        ok_counter += 1
        print("정확합니다!")
    else:
        print("오타가 있어요.")

end_time = time.time()
r = end_time - begin_time

print(f"{ok_counter}번 성공하셨습니다.")

# (타수*60)/걸린 시간(초)
y = (s * 60) // r

print("총", r, "걸렸습니다.")
print("타수=", y, "타")
