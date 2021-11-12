
def check_available(received_text: str) -> bool:
    return received_text in ("고마워", "고맙다", "땡큐", "고마워~", "고맙다", "땡큐~")

def make_response(received_text: str) -> str:
    return "그럼~ 고마워야지"

