import time

def check_available(received_text: str) -> bool:
    return received_text.startswith("초 세기:")

def time_sleep(received_text):
    s=int(received_text[5:])
    time.sleep(s)
    return f"{s}초 됐어!"
