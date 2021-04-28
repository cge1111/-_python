# 7-2 변동성 돌파 전략 백테스팅
# 레인지 계산하기

import pybithumb

df = pybithumb.get_ohlcv("BTC")
df['range'] = (df['high'] - df['low']) * 0.5
df.to_excel("btc2.xlsx")