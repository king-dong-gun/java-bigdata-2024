# file : p44_threadApp.py
# desc : PyQt5 스레드 학습용 (스레드 사용 O)

import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class BackgroundWorker(QThread) : # PyQT용 스레드
    initUiSignal = pyqtSignal(int) # 스레드로 진행할때 UI에서 초기에 처리할 초기화부분 시그널 전달
    setPgbSignal = pyqtSignal(int) # 스레드 진행시 변경되는 숫자를 UI로 전달
    setTxbSignal = pyqtSignal(str) # 스레드 진행시 화면에 출력될 문자열 UI쪽으로 전달

    def __init__(self, parent) -> None: # Background의 부모는 QtApp
        super().__init__(parent)
        self.parent = parent

    def run(self) -> None:
        maxVal = 1_000_000
        self.initUiSignal.emit(maxVal) # 값을 보내면 UI(qtApp)클래스에서 받아서 처리

        for i in range(maxVal) : 
            print(f'쓰레드 진행 >> {i}')
            self.setPgbSignal.emit(i)
            self.setTxbSignal.emit(f'쓰레드 진행 >> {i}')
            # self.pgbTask.setValue(i) # UI스레드의 권한을 백그라운드 스레드에 주지않음
            # self.txbLog.append(f'쓰레드 진행 >> {i}') # 사용불가

class qtApp(QWidget): 
        def __init__(self) -> None: 
            super().__init__() 
            self.initUI()

        def initUI(self): # Ui 파일을 로드해서 화면 디자인 사용
            uic.loadUi('./day07/testThread.ui', self) # Designer에서 꾸민 파일 가져오기
            self.setWindowTitle('ManU')
            
            self.setWindowIcon(QIcon('./images/manU.png')) # 이미지 가져오기
            
            # 버튼 시그널 처리
            self.btnStart.clicked.connect(self.btnStartClicked) # Ui파일 내 위젯은 자동완성 X

            self.show()

        def btnStartClicked(self) :
            self.btnStart.setDisabled(True)
            th =  BackgroundWorker(self)
            th.start() # 스레드 내 run()함수 실행
            th.initUiSignal.connect(self.initPgbTask) # qtApp에서 처리되는 함수
            th.setPgbSignal.connect(self.setPgbTask)
            th.setTxbSignal.connect(self.setTxbLog)

            self.btnStart.setEnabled(True)

        @pyqtSlot(str) # 슬롯은 시그널-슬롯 메커니즘의 일부, str의 인자를 받음
        def setTxbLog(self, msg) : # self.setTxbSignal.emit(f'쓰레드 진행 >> {i}') 메소드
            self.txbLog.append(msg) # 텍스트 출력

        @pyqtSlot(int)
        def setPgbTask(self, val) :
            self.pgbTask.setValue(val)
        
        @pyqtSlot(int) # pyqtSignal에서 넘어온 값을 처리해주는 부분 선언
        def initPgbTask(self, maxVal) :
            self.pgbTask.setValue(0)
            self.pgbTask.setRange(0, maxVal - 1)


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