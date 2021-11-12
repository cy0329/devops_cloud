
def check_available(received_text: str) -> bool:
    return "계산" in received_text

def make_response(received_text: str) -> str:
    return """내가 또 한 계산 하지. 어떤 계산 해줄까?
    + 덧셈
    + 뺄셈
    + 곱셈
    + 나눗셈"""

# 여기까진 아무 문제가 없다.
# 챗봇과 티키타카를 하려면 DB를 배우고 그 이해가 있어야 가능
# 내가 보낸 메시지를 DB에 저장해놓고 그에 따른 다음 출력값을 나올 수 있도록
# 해야 하는 것. 아직은 못하니 입력 : a --> 출력 : b 이 형식의 파일을
# 여러개 만들어서 티키타카를 하는 '척'을 하는 수 밖에..