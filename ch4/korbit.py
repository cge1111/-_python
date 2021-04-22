# 4 - 2 웹 스크래핑 JSON : request의 get() 함수로 얻어온 데이터는 파이썬 딕셔너리처럼 생긴 문자열 타입
import requests
import datetime  #  datetime 모듈을 임포트

r = requests.get("https://api.korbit.co.kr/v1/ticker/detailed?currency_pair=btc_krw")

print(r.text)

bitcoin = r.json()

timestamp = bitcoin['timestamp']  # 1970년 1월 1일부터 지난 시간(초)을 의미
date = datetime.datetime.fromtimestamp(timestamp/1000)
# bitcoin 딕셔너리 객체에서 'timestamp' 키를 통해 값을 얻어옵니다.

print(date)
# fromtimestamp() 함수를 사용해서 timestamp 값을 datetime 객체로 변환


print(bitcoin)
print(type(bitcoin))
print(bitcoin['last'])  # 'last'라는 key를 사용해서 최종 체결가
print(bitcoin['bid'])
print(bitcoin['ask'])
print(bitcoin['volume'])