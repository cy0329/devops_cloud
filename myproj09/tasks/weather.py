import requests
from bs4 import BeautifulSoup


def check_available(received_text: str) -> bool:
    return "날씨" in received_text

def make_response(received_text: str) -> str:
    query = "날씨"
    response_text = weather_search(query)
    return "옜다.\n" + response_text


def weather_search(query):
    naver_search_url = "https://search.naver.com/search.naver"
    params = {
        "where": "nexearch",
        "sm": "top_hty",
        "query": query,  # 검색어
    }
    res = requests.get(naver_search_url, params=params)
    return res.url