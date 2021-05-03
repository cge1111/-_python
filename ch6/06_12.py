# 06-2 변동성 돌파 전략 구현
# 단계-1: 주기적으로 현재가 얻어오기
import pybithumb
import time

while True:
    price = pybithumb.get_current_price("BTC")
    print(price)
    time.sleep(0.2)