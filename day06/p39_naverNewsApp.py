# file : p39_naverNewsApp.py
# desc : PyQt5, PyQt5Designer, Naver News검색 앱 만들기

import sys
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
            self.tblSearchResult.setItem(n, 0, QTableWidgetItem(post['title']))
            self.tblSearchResult.setItem(n, 1, QTableWidgetItem(post['link']))
            #tempDates = str(post['pubDate']).split('')
            #year = tempDates[3]
            #month = time.strptime(tempDates[2], '%b').tm_mon
            #month = f'{month : 02d}'
            #day = tempDates[1]
            #date = f'{year} - {month} - {day}'
            #self.tblSearchResult.setItem(n, 2, QTableWidgetItem(date))
            n += 1

        self.tblSearchResult.setColumnWidth(0, 465)
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