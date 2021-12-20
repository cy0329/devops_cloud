# list
# 항상 좌항과 우항의 개수가 같아야합니다.
name, age, region = ["Tom", 10, "Seoul"]

name, *__ = ["Tom", 10, "Seoul"]
# 언더바 두개는 뒤의 값들을 받지만 사용하지 않겠다는 의미

# age 값만 얻고 싶을 때
__, age, __ = ["Tom", 10, "Seoul"]
