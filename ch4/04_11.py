# 04-3 Pandas Series

# Series 인덱싱/슬라이싱

from pandas import Series

date = ['2018-08-01', '2018-08-02', '2018-08-03', '2018-08-04', '2018-08-05'] 
xrp_close = [512, 508, 512, 507, 500] 
s = Series(xrp_close, index=date) 

print(s.index) 
print(s.values) 