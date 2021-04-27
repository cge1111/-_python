import pyupbit     # 과거 데이터 조회, 

# (시가(open), 고가(high), 저가(low), 종가(close), 거래량(volume))
# get_ohlcv() 함수는 가상화폐의 티커를 입력받아 OHLCV 데이터를 판다스 DataFrame으로 반환
df = pyupbit.get_ohlcv("KRW-BTC") 
print(df)


# interval 옵션으로 월/주/일/분봉 중 하나를 선택
df  = pyupbit.get_ohlcv("KRW-BTC", interval = "minute") 
print(df)


# count 옵션은 가져오려는 데이터의 개수를 지정하는 데 사용합니다. 만약 최근 5일간의 데이터만 조회
df = pyupbit.get_ohlcv("KRW-BTC", count = 5) 
print(df)