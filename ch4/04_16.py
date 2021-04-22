# 04-4 Pandas DataFrame

# DataFrame 생성
from pandas import DataFrame

data = {'open': [100, 200], "high" : [110, 210]}
df  = DataFrame(data, index = ["2018-01-01", "2018-01-02"])
print(df)