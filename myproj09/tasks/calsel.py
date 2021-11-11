
def check_available(received_text: str) -> bool:
    return "계산" in received_text

def make_response(received_text: str) -> str:
    return "내가 또 한 계산 하지. 어떤 계산 해줄까?\n 덧셈\n 뺄셈\n 곱셈\n 나눗셈"

# 여기까진 아무 문제가 없다.