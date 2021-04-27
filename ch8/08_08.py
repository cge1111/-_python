# 주문 취소
import pyupbit

access_key = "57xwiVxqYFHuqoiwR5MIZAPZEXF67RxJO6mMZ0Yg" 
secret_key = "ZIrW1DpUliu295b7xqlC6CbhIG2K4xak4PEihyt3" 

upbit = pyupbit.Upbit(access_key, secret_key)
# 주문 메서드를 호출하면 uuid 값이 리턴됨을 확인, uuid를 갖는 주문 취소할 수 있습니다.
ret = upbit.cancel_order('cc52be46-1000-4126-aee7-9bfafb867682')
print(ret)