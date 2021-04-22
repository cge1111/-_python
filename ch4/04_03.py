# 04-2 웹 스크래핑 (2) : 인터넷 주소 끌어올 때

# TML 문서 다운로드 및 파싱
import requests
from bs4 import BeautifulSoup

url = "http://finance.naver.com/item/main.nhn?code=000660"
html = requests.get(url).text

soup = BeautifulSoup(html, "html5lib")
# tags = soup.select('#_per')
tags = soup.select('#_dvr')
tag = tags[0]
print(tag.text)