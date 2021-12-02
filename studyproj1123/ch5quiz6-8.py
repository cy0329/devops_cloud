# 6. % 포매팅 사용해서 출력
names = ["Duck", "Gourd", "Spitz"]
for name in names:
    print("%sy Mc%sface" % (name, name))

print("======================")
# 7. format() 매서드 사용하여 출력
for name in names:
    print("{}y Mc{}face".format(name, name))

print("======================")
# 8. f-문자열 사용해 출력
for name in names:
    print(f"{name}y Mc{name}face")
