import pybithumb

orderbook = pybithumb.get_orderbook("BTC")  # 각각이 호가(수량과 가격)
bids = orderbook['bids']           # 매수 호가 및 잔량 반복문

for bid in bids:
    price = bid['price']           # 딕셔너리에서 'price'라는 키로 인덱싱
    quant = bid['quantity']        # 딕셔너리에서 'quantity'라는 키로 인덱싱
    print("비트코인 매수호가:",price, "비트코인 매수잔량:",quant)


print("\n")

asks = orderbook['asks']           # 매도 호가 및 잔량

for ask in asks:
    price = bid['price']           # 딕셔너리에서 'price'라는 키로 인덱싱
    quant = bid['quantity']        # 딕셔너리에서 'quantity'라는 키로 인덱싱
    print("비트코인 매도호가:",price, "비트코인 매도잔량:",quant)


