# 06-2 변동성 돌파 전략 구현
# 단계-3: 자정에 목표가 갱신하기

import time
import datetime

now = datetime.datetime.now()
# 프로그램이 시작할 때 실행되는 코드로 다음날 자정 시각을 계산하기 위해 현재 시각을 얻어옵니다.
mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
# 다음날 자정의 시각을 계산해서 datetime 객체로 저장합니다.

while True:
    now = datetime.datetime.now()
    # while문 안에서 반복해서 현재 시각을 얻어옵니다.
    if now == mid:
    # datetime의 비교 연산을 사용해서 얻어온 현재 시각이 자정인지 체크합니다.
        print("정각입니다.")
        now = datetime.datetime.now()
        mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
        # 자정이라면 다음날의 자정 시각을 계산합니다.

    print(now, "vs", mid)  # 현재 시각과 다음날 자정 시각을 출력합니다.
    time.sleep(1)