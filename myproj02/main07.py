def 부가세_계산(금액):
    부가세 = 금액 // 11
    return 부가세  # <<이걸 써주어야함
    # return none과 return이 없는것은 같다.


# v = int(input("계산할 금액 : ")) 사용, 2줄로 해도 됨
부가세 = 부가세_계산(int(input("계산할 금액 : ")))

print(f"부가세 : {부가세}")
