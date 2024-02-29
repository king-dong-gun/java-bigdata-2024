# file : p44_nothreadApp.py
# desc : PyQt5 스레드 학습용 (스레드 사용 X)
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
        uic.loadUi('./day07/testThread.ui', self) # Designer에서 꾸민 파일 가져오기
        self.setWindowTitle('No Thread App')
        
        # 버튼 시그널 처리
        self.btnStart.clicked.connect(self.btnStartClicked) # Ui파일 내 위젯은 자동완성 X

        self.show()

    def btnStartClicked(self) :
        self.pgbTask.setValue(0) # 재설정
        self.pgbTask.setRange(0, 999_999) # 프로그레스 바 범위 정하기
        self.btnStart.setDisabled(True)
        # UI(메인)스레드가 화면을 그릴 수 있는 여유가 없음(응답없음 발생)
        for i in range(0, 1_000_000) : # 0~999,999까지
            print(f'맨유 우승 횟수 >> {i}')
            self.pgbTask.setValue(i)
            self.txbLog.append(f'맨유 우승 횟수 >> {i}')
        self.btnStart.setEnabled(True)


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