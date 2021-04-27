import pybithumb

orderbook = pybithumb.get_orderbook("BTC")  # 호가
print(orderbook)

for k in orderbook: # orderbook 딕셔너리에는 다음과 같이 다섯 개의 키가 저장
    print(k)

# print(orderbook['payment_currency'])
