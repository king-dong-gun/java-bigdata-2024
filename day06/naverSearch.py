# file: naverSearch.py
# desc: 네이버 검색 API용 클래스

from urllib.request import Request, urlopen
from urllib.parse import quote # 글자를 유니코드(utf-8)로 인코딩
import datetime
import json # json 학습 필요
import ssl # 보안 문제로 인한 import

class naverSearch :
    def __init__(self) -> None:
        print('Naver API 클래스 생성')

    # URL로 검색 시작하는 함수
    def getRequestUrl(self, url) : # 클래스 내에서 사용할 함수
        ssl._create_default_https_context = ssl._create_unverified_context # ssl 함수 생성

        req = Request(url)
        req.add_header('X-Naver-Client-Id', 'h6HHZDuoeZ9IJHimmDzI') # 자신의 애플리케이션 클라이언트 아이디 입력 칸
        req.add_header('X-Naver-Client-Secret', '8ERho_o5iB') # 자신의 애플리케이션 클라이언트 시크릿 입력 칸

        try:
            res = urlopen(req)
            if res.status == 200 :
                print(f'[{datetime.datetime.now()}]: URL 요청 성공')
                return res.read().decode('utf-8')
        except Exception as e :
            print(f'[{datetime.datetime.now()}]: URL 요청 오류!!{e.args}')
            return None # 예외가 발생하면 아무값도 돌려주지 않음 -> None값을 넘김

    # 실제 동작 함수
    def getSearchResult(self, searchWord) :
        baseUrl = 'https://openapi.naver.com/v1/search/news.json'
        params = f'?query={quote(searchWord)}&start=1&display=20'  # 띄어쓰기 X 다 붙혀써야함, display -> 칼럼 수
        finalUrl = baseUrl + params

        result = self.getRequestUrl(finalUrl) 
        if result != None : # 예외가 발생하지 않았으면
            return json.loads(result)
        else :
            return None