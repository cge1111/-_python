# Bithumb 클래스 객체 생성하기 -- 매도
import pybithumb
import time

con_key = "d53db84d643e7c314055ad2fe316c454"
sec_key =  "7662d210f14c8a13ae2c680e0738ea5f"

bithumb = pybithumb.Bithumb(con_key, sec_key)

order = bithumb.sell_limit_order("BTC", 4000000000, 1)
print(order)
