# 7-1 백테스팅을 위한 데이터 준비하기
# 가상화폐 일봉 데이터 얻기

import pybithumb

df = pybithumb.get_ohlcv("BTC")
df.to_excel("btc.xlsx")