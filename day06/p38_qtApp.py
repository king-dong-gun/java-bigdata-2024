# file : p38_qtApp.py
# desc : PyQt5, QtDesigner 같이 사용(계속)
'''
PyQt5 -> Qt를 파이썬에서 쓸수 있도록 만든 라이브러리
Qt -> C,C++ 사용할 GUI(WinApp) 프레임워크(멀티플랫폼)

설치 > pip install PyQt5
설치 > pip install PyQt5Designer
'''
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class qtApp(QWidget): 
    def __init__(self) -> None: 
        super().__init__() 
        self.initUI()

    def initUI(self): # Ui 파일을 로드해서 화면 디자인 사용
        uic.loadUi('./day06/firstApp.ui', self) # Designer에서 꾸민 파일 가져오기
        self.setWindowIcon(QIcon('./images/windows.png'))
        
        # 버튼 시그널 처리
        self.btnMsg.clicked.connect(self.btnMsgClicked) # Ui파일 내 위젯은 자동완성 X

        self.show()

    def btnMsgClicked(self) :
        QMessageBox.about(self, 'Qt디자이너', '클릭하였습니다!!!!') # about 함수 -> 3개의 인자를 가져야함
        self.label.setText('Old Trafford')

    def closeEvent(self, QCloseEvent) -> None: # 우리식으로 오버라이드 (재정의)
        re = QMessageBox.question(self, '종료확인', '종료하시겠습니까?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes : # 닫음
            QCloseEvent.accept()
        else :
            QCloseEvent.ignore() # 무시

app = QApplication(sys.argv) # 
inst = qtApp() # 객체 생성
app.exec_() # 실행

# QyQt5Designer 위젯- 푸쉬버튼