import pyupbit 

# tickers = pyupbit.get_tickers() // 비트코인 티커 조회 가격
# tickers = pyupbit.get_tickers(fiat = "KRW")  # 원화 시장에서 주문 가능한 티커 목록

# print(tickers)


price = pyupbit.get_current_price("KRW-XRP")  # 현재가 조회
print("현재 리플의 가격은", price, "입니다.")

price = pyupbit.get_current_price("KRW-BTC")  # 현재가 조회
print("현재 비트코인의 가격은", price, "원 입니다.")

price = pyupbit.get_current_price(["KRW-XRP", "KRW-XRP"])
print(price)




