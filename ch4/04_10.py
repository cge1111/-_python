# 04-3 Pandas Series
# 판다스 (Pandas) 란?  1차원 데이터를 다루는 Series 타입과 2차원 데이터를 위한 DataFrame 타입을 제공합
# 데이터 분석을 위한 다양한 메서드를 제공

# Series 생성할 때 인덱스를 지정하기

from pandas import Series

# data = [100, 200, 300, 400]
# s = Series(data)
# print(type(s))
# print(s)

date = ['2018-08-01', '2018-08-02', '2018-08-03', '2018-08-04', '2018-08-05'] 
xrp_close = [512, 508, 512, 507, 500] 
s = Series(xrp_close, index=date) 

print(s) # index값이 생략되어있다.

print(s[0])
print(s['2018-08-01'])