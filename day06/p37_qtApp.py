# file : p37_qtApp.py
# desc : PyQt5 앱 만들기 (계속)
'''
PyQt5 -> Qt를 파이썬에서 쓸수 있도록 만든 라이브러리
Qt -> C,C++ 사용할 GUI(WinApp) 프레임워크(멀티플랫폼)

설치 > pip install PyQt5
'''
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import *

class qtApp(QWidget): 
    def __init__(self) -> None: 
        super().__init__() 
        self.initUI()

    def initUI(self):
        self.setGeometry((1920 - 300)//2, (1080 - 300)//2, 320, 230) # 해상도 1920 x 1080에서 정중앙에 위치
        self.setWindowTitle('세번째 Qt앱')
        self.setWindowIcon(QIcon('./images/manU.png'))
        # 화면 UI에서 추가 or 변경할 것
        btn01 = QPushButton('클릭', self) # 버튼 객체 생성
        btn01.setGeometry(210, 180, 100, 40) # 버튼 위치 생성
        btn01.clicked.connect(self.btn01Clicked) # btn01 클릭 시그널이 발생하면 이를 처리하는 함수 연결 시켜줘야함
        self.show()

    def btn01Clicked(self) :
        QMessageBox.about(self, '버튼 클릭', '버튼을 눌렀습니다.')

    def closeEvent(self, QCloseEvent) -> None: # 우리식으로 오버라이드 (재정의)
        re = QMessageBox.question(self, '종료확인', '종료하시겠습니까?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes : # 닫음
            QCloseEvent.accept()
        else :
            QCloseEvent.ignore() # 무시
            # QMessageBox.about(self, '취소', '종료안할건데 왜 누름?') # No 창에다가 또 QMessageBox 넣을수 있음

app = QApplication(sys.argv) # 
inst = qtApp() # 객체 생성
app.exec_() # 실행