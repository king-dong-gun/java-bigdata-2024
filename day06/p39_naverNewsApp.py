# file : p39_naverNewsApp.py
# desc : PyQt5, PyQt5Designer, Naver News검색 앱 만들기

import sys
import time
from PyQt5 import QtCore, QtGui, QtWidgets, uic 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import webbrowser # 기본 웹브라우저 모듈
from naverSearch import naverSearch
import datetime


class qtApp(QWidget): 
    def __init__(self) -> None: 
        super().__init__() 
        self.initUI()

    def initUI(self): # Ui 파일을 로드해서 화면 디자인 사용
        uic.loadUi('./day06/naverNews.ui', self) # Designer에서 꾸민 파일 가져오기
        self.setWindowIcon(QIcon('./images/news.png')) # 아이콘 파일에 맞춰 변경
        
        # 버튼 시그널 처리
        self.btnSearch.clicked.connect(self.btnSearchClicked) 
        self.txtSearchWord.returnPressed.connect(self.btnSearchClicked) # 검색 버튼 시그널 함수를 연결 (enter)
        self.tblSearchResult.itemSelectionChanged.connect(self.tblResultSelected)

        self.show()
    
    def tblResultSelected(self) : # 테이블 클릭시 처리
        selectRow = self.tblSearchResult.currentRow() # 현재 선택된 행의 인덱스
        url = self.tblSearchResult.item(selectRow, 1).text()
        # QMessageBox.about(self, 'popup', url)
        webbrowser.open(url)

    def btnSearchClicked(self) : # 검색버튼 클릭시 처리
        searchWord = self.txtSearchWord.text().strip()
        print(searchWord)

        if(len(searchWord)) == 0 :  # 입력 검증
            QMessageBox.about(self, '네이버 검색', '검색어를 입력하세요.')
            return # 함수 탈출
        

        print(searchWord)
        # QMessageBox.about(self, '네이버 검색', '검색시작!!!') # about 함수 -> 3개의 인자를 가져야함
        
        # 검색 시작
        api = naverSearch() # api 객체 생성
        jsonSearch = api.getSearchResult(searchWord)
        # print(jsonSearch)
        self.makeTable(jsonSearch) # 검색 결과로 리스트뷰를 만드는 함수

    
    def makeTable(self, data) :
        result = data['items'] # naver 검색 결과의 키 items의 값들만 활용하는 함수
        # tblSearchResult 리스트뷰 작업 시작
        self.tblSearchResult.setColumnCount(3) 
        self.tblSearchResult.setRowCount(len(result)) # 10개면 10개
        self.tblSearchResult.setHorizontalHeaderLabels(['기사제목', '뉴스링크', '게시일자'])

        n = 0

        for post in result :
            # html 태그, 특수문자 삭제코드 (<b>, </b>, &lt;[<], &gt;[>], &qout;, &nbsp;[])
            title = str(post['title']).replace('<b>', '').replace('</b>', '').replace('&quot;', '"')

            self.tblSearchResult.setItem(n, 0, QTableWidgetItem(title))
            self.tblSearchResult.setItem(n, 1, QTableWidgetItem(post['link']))

            #현재 날짜 Thu, 29, Feb, 2024, 09:00:00 +09:00:00 -> 2024-02-29 로 변경

            # Os문제로 if문으로 Jan -> 1로 바꿔주는 함수
            def changeMonthFormat(month):
                if month == "Jan":
                    return "1"
                elif month == "Feb":
                    return "2"
                elif month == "Mar":
                    return "3"
                elif month == "Apr":
                    return "4"
                elif month == "May":
                    return "5"
                elif month == "Jun":
                    return "6"
                elif month == "Jul":
                    return "7"
                elif month == "Aug":
                    return "8"
                elif month == "Sep":
                    return "9"
                elif month == "Oct":
                    return "10"
                elif month == "Nov":
                    return "11"
                elif month == "Dec":
                    return "12"
            tempDates = str(post['pubDate']).split(' ')
            year = tempDates[3]
            month = time.strptime(changeMonthFormat(tempDates[2]), "%m").tm_mon # Feb, Mar 같은 영어 단축이름을 2, 3 월에 대한 숫자로 변경하는 로직
            month = f'{month : 02d}' # 월에 대한 두자리로 만들때 앞에 0 -> 01, 02, 03
            day = tempDates[1]
            date = f'{year} - {month} - {day}'
            self.tblSearchResult.setItem(n, 2, QTableWidgetItem(date))
            n += 1


        self.tblSearchResult.setColumnWidth(0, 430) # QTable에 가로 스크롤 넓이 조절
        self.tblSearchResult.setColumnWidth(1, 200)
        self.tblSearchResult.setEditTriggers(QAbstractItemView.NoEditTriggers) # 컬럼 더블클릭 금지


    def closeEvent(self, QCloseEvent) -> None:
        re = QMessageBox.question(self, '종료확인', '종료하시겠습니까?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes : # 닫음
            QCloseEvent.accept()
        else :
            QCloseEvent.ignore() # 무시

app = QApplication(sys.argv) # 
inst = qtApp() # 객체 생성
app.exec_() # 실행