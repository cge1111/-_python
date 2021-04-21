# 호가 조회
import pyupbit


# 매수호가(bid)와 매도호가(ask) 조회는 get_orderbook() 함수, 10호가 데이터 얻을 수 있다.
orderbook = pyupbit.get_orderbook("KRW-BTC")
bids_asks = orderbook[0]['orderbook_units']   # 10호가 데이터 리스트 객체를 bids_asks라는 변수가 바인딩


for bid_ask in bids_asks:
    print(bid_ask)
    print("\n")
# ask_price는 매도 호가이고 bid_price는 매수 호가, 
# ask_size와 bid_size는 매도 호가 수량과 매수 호가 수량