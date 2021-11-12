from . import weather

def test_weather():
    assert weather.check_available("날씨 어때")
    assert weather.make_response("날씨 어때") == '옜다.\n'+"https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%82%A0%EC%94%A8"