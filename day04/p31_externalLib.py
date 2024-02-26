# file: p31_externalLib.py
# desc: 외부라이브러리 사용법

# > pip install LibName
# Successfully intalled / Requirement already satisfaied 가 나와야함
# > pip uninstall LibName
# Successfully uninstalled 가 나와야함

from faker import Faker

fake = Faker('ko-KR') # 한국어 설정
print(fake.name())
print(fake.address())
# print(fake.profile())

dummyData = [(fake.name(),fake.address())]
print(dummyData)

## urllib3 외부 웹페이지 분석 모듈
import requests
from bs4 import BeautifulSoup

#res = requests.get('http://www.naver.com')
#print(res.status_code)
#print(res.content) # 내용 가져오기

res = requests.get('http://www.google.com')
if res.status_code == 200 :
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)
