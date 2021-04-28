# Bithumb 클래스 객체 생성하기
import pybithumb
import time

con_key = "d53db84d643e7c314055ad2fe316c454"
sec_key =  "7662d210f14c8a13ae2c680e0738ea5f"

bithumb = pybithumb.Bithumb(con_key, sec_key)

# 잔고 조회
for ticker in pybithumb.get_tickers() :
    balance = bithumb.get_balance(ticker)
    print(ticker, ":", balance)
    time.sleep(0.1)




