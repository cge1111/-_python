# Bithumb 클래스 객체 생성하기 -- 매수
import pybithumb
import time

con_key = "d53db84d643e7c314055ad2fe316c454"
sec_key =  "7662d210f14c8a13ae2c680e0738ea5f"

bithumb = pybithumb.Bithumb(con_key, sec_key)

# 지정가 매수
# order = bithumb.buy_market_order("BTC", 1)
# print(order)

# 본인 계좌의 보유 원화를 조회
krw = bithumb.get_balance("BTC")[2]
orderbook = pybithumb.get_orderbook("BTC")

asks = orderbook['asks']
sell_price = asks[0]['price']
unit = krw/sell_price
print(unit)