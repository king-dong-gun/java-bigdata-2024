# file : p48_transApp.py
# desc : PyQt5 구글 번역 앱

import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from googletrans import Translator

class qtApp(QWidget): 
    def __init__(self) -> None: 
        super().__init__() 
        self.initUI()
        self.myTrans = Translator() # 구글 번역기 객체 생성

    def initUI(self): # Ui 파일을 로드해서 화면 디자인 사용
        uic.loadUi('./day07/transApp.ui', self) # Designer에서 꾸민 파일 가져오기
        self.setWindowTitle('Google 번역기')
        self.setWindowIcon(QIcon('./images/manU.png'))
        
        # 버튼 시그널 처리
        self.btnTrans.clicked.connect(self.btnTransClicked) # Ui파일 내 위젯은 자동완성 X
        self.txtBaseText.returnPressed.connect(self.btnTransClicked)

        self.show()

    def btnTransClicked(self) :
        # QMessageBox.about(self,'번역','번역시작')
        text = self.txtBaseText.text().strip()
        if len(text) != 0 :
            result = self.myTrans.translate(text, src='auto', dest='en')
            self.txbResult.append(result.text)



    def closeEvent(self, QCloseEvent) -> None:
        re = QMessageBox.question(self, '종료확인', '종료하시겠습니까?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes : # 닫음
            QCloseEvent.accept()
        else :
            QCloseEvent.ignore() # 무시

app = QApplication(sys.argv) # 
inst = qtApp() # 객체 생성
app.exec_() # 실행

