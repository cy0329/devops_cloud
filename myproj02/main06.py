def gugudan(num):
    # num = 2
    print(f"---< {num}단 >---")
    for i in range(1, 10):
        print(f"{num}*{i}={num*i}")


# gugudan(2)
# gugudan(3)
# gugudan(4)...

for i in range(2, 10):
    gugudan(i)
