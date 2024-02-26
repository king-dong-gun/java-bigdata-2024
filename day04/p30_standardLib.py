# file: p30_standardLib.py
#  desc: 표준 라이브러리(빌트인) 학습

import datetime
import time
import random

print(datetime.date(2024, 2, 26))  # 현재의 OS에 맞춰서 날짜형으로 변경

# 정말 많이 씀
curr = datetime.datetime.now() # 현재의 년,월,일,시,분,초를 알려줌
print(curr)

print(curr.weekday()) # 0은 월요일 ~ 6은 일요일
print(curr.year)
print(curr.month)
print(curr.day)
print(curr.minute)
print(curr.second)

print(f'{curr.year}년 {curr.month:02d}월 {curr.day}일 {curr.hour}시 {curr.minute}분')

curr2 = time.localtime() # time으로 찾는 localtime()은 잘 안쓰임
print(curr2)

## 무지막지하게 많이 쓰임
for i in range(5) :
    print(f'{i + 1} 출력')
    # time.sleep(2) # 2초씩 잠시 멈춤

##
print(random.random())
print(random.randint(1, 45, ))

## 로또

total = []
result = []

for i in range(5) :
    while True :
        val = random.randint(1, 45)
        while val not in result :
            result.append(val)
        if len(result) == 6 :
            break
    result.sort()
    total.append(result)
    result=[]
print(total)

## 내부라이브러리중 웹사이트 분석용
# import urllib
# 요청(request) > 응답(respone)
from urllib.request import Request, urlopen

req = Request('https://www.naver.com')
res = urlopen(req)

print(res.status) # 응답코드 200 OK
print(res.read()) # 내용 가져오기
