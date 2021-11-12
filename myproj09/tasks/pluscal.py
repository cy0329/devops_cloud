
def check_available(received_text: str) -> bool:
    return received_text == "덧셈"

def make_response(received_text: str):
    return "더할 숫자들을 <덧셈:숫자1,숫자2,숫자3,~~> 이런식으로 써봐"
