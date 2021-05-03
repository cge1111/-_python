# 06-2 변동성 돌파 전략 구현
# 단계-2: 목표가 계산하기

# import pybithumb

df = pybithumb.get_ohlcv("BTC")
yesterday = df.iloc[-2]

today_open = yesterday['close']
yesterday_high = yesterday['high']
yesterday_low = yesterday['low']
target = today_open + (yesterday_high - yesterday_low) * 0.5
# 래리 윌리엄스 변동성 돌파 전략의 목표가를 계산합니다. (당일 시가 + 레인지 x 0.5)
print(target)


# 코드의 재사용을 위해 목표가를 계산하는 부분을 함수로 정리
def get_target_price(ticker):
    df = pybithumb.get_ohlcv(ticker)
    yesterday = df.iloc[-2]

    today_open = yesterday['close']
    yesterday_high = yesterday['high']
    yesterday_low = yesterday['low']
    target = today_open + (yesterday_high - yesterday_low) * 0.5
    return target
