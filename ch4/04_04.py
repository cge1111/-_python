# 04 - 2 웹 스크래핑 (2) : 인터넷 주소 끌어올 때

# ID가 있는 일반적인 경우에 대한 스크래핑

# 네이버 금융의 하이닉스 주가 정보 (per, 배당수익률)
import requests
from bs4 import BeautifulSoup

def get_per(code):
    url = "http://finance.naver.com/item/main.nhn?code=" + code
    html = requests.get(url).text

    soup = BeautifulSoup(html, "html5lib")
    tags = soup.select('#_per')
    tag = tags[0]
    return float(tag.next)


def get_dividend(code):
    url = "http://finance.naver.com/item/main.nhn?code=" +code
    html = requests.get(url).text

    soup = BeautifulSoup(html, "html5lib")
    tags = soup.select('#_dvr')
    tag = tags[0]
    return float(tag.next)

print(get_per("000660"))
print(get_dividend("000660"))