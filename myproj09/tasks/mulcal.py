
def check_available(received_text: str) -> bool:
    return received_text == "곱셈"

def make_response(received_text: str):
    return "곱할 숫자들을 <곱셈:숫자1,숫자2,숫자3,~~~> 이런식으로 써봐"
