def check_available(received_text: str) -> bool:
    return received_text == "help"


def make_response(received_text: str) -> str:
    return """
    <기본 명령어 목록>
    0. /start
    1. 야
    2. 뭐해
    3. "날씨"가 들어간 말
    4. "계산"이 들어간 말
    5. 고마워(~), 고맙다(~), 땡큐(~) 등
    """
