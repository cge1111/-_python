# 매수/매도, 주문 취소
import pyupbit

access_key = "57xwiVxqYFHuqoiwR5MIZAPZEXF67RxJO6mMZ0Yg" 
secret_key = "ZIrW1DpUliu295b7xqlC6CbhIG2K4xak4PEihyt3" 


# 지정가 매수를 위해서는 buy_limit_order() 메서드
# 지정가 매도를 위해서는 sell_limit_order() 메서드를 사용
upbit = pyupbit.Upbit(access_key, secret_key)
ret = upbit.buy_limit_order("KRW-XRP", 100, 20)
print(ret)


