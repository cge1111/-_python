# 자정에 목표가 갱신하기
import datetime    # datetime 모듈을 import 합니다.

# dt = datetime.datetime(2018, 12, 1)  # datetime 클래스의 초기화자로 년/월/일 세 개의 값을 전달합니다.
now = datetime.datetime.now()   # now() 메서드로 현재 시각을 얻어옵니다.
mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
#  00:00:00 초의 datetime 객체를 생성하고, 1일의 시간을 더해 다음 날 자정으로 만듭니다. timedelta(1)이 1일의 시간을 의미합니다.
print(now)
print(mid)