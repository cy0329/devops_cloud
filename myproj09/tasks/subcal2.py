import re
from functools import reduce

def check_available(received_text: str):
    return received_text.startswith("뺄셈:")

def make_response(received_text: str):
    line = received_text[3:]
    nums = map(int, re.findall(r"\d+", line))
    calculated_num = reduce(lambda x,y: x-y, nums)
    return str(calculated_num)
