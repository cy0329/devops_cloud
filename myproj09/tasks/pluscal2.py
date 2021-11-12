import re

def check_available(received_text: str):
    return received_text.startswith("덧셈:")

def make_response(received_text: str):
    line = received_text[3:]
    calculated_num = sum(map(int, re.findall(r"\d+", line)))
    return str(calculated_num)
