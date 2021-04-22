# 04 - 2 웹 스크래핑 (2) : 인터넷 주소 끌어올 때

# ID가 있는 일반적인 경우에 대한 스크래핑

# 네이버 금융의 하이닉스 주가 정보 (per, 배당수익률)
import requests
from bs4 import BeautifulSoup

url = "https://www.bithumb.com/"
html = requests.get(url).text

soup = BeautifulSoup(html,"html5lib")

tag = soup.select("#assetRealBTC_KRW")[0]
print(tag.text)
tag = soup.select("#assetRealETH_KRW")[0]
print(tag.text)



