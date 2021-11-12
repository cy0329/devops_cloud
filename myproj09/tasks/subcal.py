
def check_available(received_text: str) -> bool:
    return received_text == "뺄셈"

def make_response(received_text: str):
    return "<뺄셈:숫자1-숫자2> 이런식으로 써봐"
