import pybithumb

btc = pybithumb.get_ohlcv("BTC")  # 거래소 과거 시세 얻어오기
close = btc['close']              # 날짜별 종가
print(close)