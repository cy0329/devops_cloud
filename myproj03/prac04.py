for num in range(2, 10):
    for i in range(1, 10):
        print(f"{num}*{i}={num*i}")
        if num == i:
            break
