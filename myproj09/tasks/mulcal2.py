import re
from functools import reduce

def check_available(received_text: str):
    return received_text.startswith("곱셈:")

def make_response(received_text: str):
    numbers = map(int, re.findall(r"\d+", received_text[3:]))
    calculated_num = reduce(lambda x, y: x*y, numbers, 1)
    return str(calculated_num)
