# file : p47_qrCodeApp.py
# desc : PyQt5 QR코드앱

import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import qrcode

class qtApp(QWidget): 
    def __init__(self) -> None: 
        super().__init__() 
        self.initUI()

    def initUI(self): # Ui 파일을 로드해서 화면 디자인 사용
        uic.loadUi('./day07/qrApp.ui', self) # Designer에서 꾸민 파일 가져오기
        self.setWindowTitle('Old Trafford 입장 QR Code')
        
        # 버튼 시그널 처리
        self.btnGenerate.clicked.connect(self.btnGenerateClicked) # Ui파일 내 위젯은 자동완성 X

        self.show()

    def btnGenerateClicked(self) :
        data = self.txtQrData.text()

        if len(data.strip()) == 0 :
            QMessageBox.about(self,'경고','무단출입')
            return
        else :
            imgPath = './images/qr.png'
            qrImage = qrcode.make(data)
            qrImage.save(imgPath)
            img = QPixmap(imgPath)
            self.lblQrCode.setPixmap(QPixmap(img).scaledToWidth(300))


    def closeEvent(self, QCloseEvent) -> None:
        re = QMessageBox.question(self, '종료확인', '종료하시겠습니까?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes : # 닫음
            QCloseEvent.accept()
        else :
            QCloseEvent.ignore() # 무시

app = QApplication(sys.argv) # 
inst = qtApp() # 객체 생성
app.exec_() # 실행

