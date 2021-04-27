import pybithumb

btc = pybithumb.get_ohlcv("BTC")       # 이동평균 계산하기
close = btc['close']              

window = close.rolling(5)
ma5 = window.mean()
print(ma5)

# ma5 = close.rolling(5).mean()