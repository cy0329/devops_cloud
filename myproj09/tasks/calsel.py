
def check_available(received_text: str) -> bool:
    return "계산" in received_text

def make_response(received_text: str) -> str:
    return "내가 또 한 계산 하지. 어떤 계산 해줄까? 1. 덧셈, 2. 뺄셈, 3. 곱셈, 4. 나눗셈"

