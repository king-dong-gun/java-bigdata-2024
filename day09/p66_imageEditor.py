# file: p66_imageEditor.py
# desc: PyQt 이미지 에디터

'''
qrc파일 사용 >>>> pyrcc5 "resources.qrc"

imutils
pip3 install imutils
'''


import sys
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QMouseEvent, QCloseEvent
from PyQt5.QtWidgets import *
# 리소스 파일 추가
import resources_rc
# OpenCV 추가
import cv2, imutils

class windowApp(QMainWindow) : #QWidget 아님!!
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        self.initSignal()
    
    def initUI(self) :
        # uic.loadUi('./day09/pyNewPaint.ui', self) # VSCode 실행용
        uic.loadUi('/Users/kimdonggun/Desktop/study/source/java-bigdata-2024/day09/pyNewPaint.ui', self) # pyInstaller 실행용 >> UI 절대경로
        self.setWindowTitle('imageEditor v.0.5')
        # self.setWindowIcon(QIcon('./day09/imgs/editor.png'))
        self.setWindowIcon(QIcon('/Users/kimdonggun/Desktop/study/source/java-bigdata-2024/day09/imgs/editor.png')) # pyInstaller 실행용 >> 이미지 절대경로

        ## 이미지 추가 / 여러가지 UI에 대한 초기화
        pixmap = QPixmap('./day09/hmba.jpg').scaledToHeight(451)
        self.lblCanvas.setPixmap(pixmap)
        self.brushColor = Qt.red # 기본색 > 빨강
        # UI 초기화 끝
        self.show()

    def initSignal(self) :
        # 메뉴/툴바 액션에 대한 시그널처리 함수 선언
        self.action_New.triggered.connect(self.actionNewClicked)
        self.action_Open.triggered.connect(self.actionOpenClicked)
        self.action_Save.triggered.connect(self.actionSaveClicked)
        self.action_Close.triggered.connect(self.actionCloseClicked)
        self.action_Red.triggered.connect(self.actionRedClicked)
        self.action_Green.triggered.connect(self.actionGreenClicked)
        self.action_Blue.triggered.connect(self.actionBlueClicked)
        self.action_About.triggered.connect(self.actionAboutClicked)
        # 변환 메뉴 추가
        self.action_GrayScale.triggered.connect(self.actionGrayScaleClicked)
        self.action_Blur.triggered.connect(self.actionBlurClicked)

    def actionBlurClicked(self) :
        tempPath = './temp.png'
        pixmap = self.lblCanvas.pixmap() # 라벨에 있는 그림을 pixmap 변수에 저장
        pixmap.save(tempPath)
        image = cv2.imread(tempPath)
        blur = cv2.blur(image, (10,10))
        blurImg = QImage(blur, blur.shape[1], blur.shape[0], blur.strides[0], QImage.Format_BGR888)
        self.lblCanvas.setPixmap(QPixmap.fromImage(blurImg))


    def actionGrayScaleClicked(self) :
        # image = cv2.imread()
        QMessageBox.about(self, '알림', '그레이스케일로')
        # temp.png 와 같은 형태로 임시 이미지 저장 >> openCV로 불러옴 >> 그레이스케일로 변경함 >>
        # >> 변경한 이미지를 lblCanvas에 다시 pixmap으로 변환 >> lblCanvas에 올림
        tempPath = './day09/temp.png'
        pixmap = self.lblCanvas.pixmap() # 라벨에 있는 그림을 pixmap 변수에 저장
        pixmap.save(tempPath)
        image = cv2.imread(tempPath)
        grayImg = QImage(image, image.shape[1], image.shape[0], image.strides[0], QImage.Format_Grayscale8)
        self.lblCanvas.setPixmap(QPixmap.fromImage(grayImg))

    def actionNewClicked(self) :
        canvas = QPixmap(self.lblCanvas.width(), self.lblCanvas.height())
        canvas.fill(QColor('black'))
        self.lblCanvas.setPixmap(canvas) # New 버튼 누를때마다 검정색 화면으로 초기화

    def actionOpenClicked(self) :
        image = QFileDialog.getOpenFileName(self, '이미지열기', ', ', 'Image file(*.jpg;*.png;*gif)')
        imagePath = image[0]
        pixmap = QPixmap(imagePath).scaledToHeight(471)
        self.lblCanvas.setPixmap(pixmap)
        self.lblCanvas.adjustSize() # 가져온 사진 라벨 크기 맞추기 > 471

    def actionSaveClicked(self) :  
        filePath, _ = QFileDialog.getSaveFileName(self, '이미지저장', ', ', 'Image file(*.jpg;*.png;*gif)')
        if filePath == '' : return
        pixmap = self.lblCanvas.pixmap() # 캔버스에 표시된 이미지 객체 가져오기
        pixmap.save(filePath)

    def actionCloseClicked(self) :
        QMessageBox.about(self, '알림', '나가기!!')

    def actionRedClicked(self) :
        self.brushColor = Qt.red

    def actionGreenClicked(self) :
        self.brushColor = Qt.green

    def actionBlueClicked(self) :
        self.brushColor = Qt.blue

    def actionAboutClicked(self) :
        QMessageBox.about(self, '알림', '프로그램 정보!!')

    def mouseMoveEvent(self, e)-> None:
        print(e.x(), e.y()-(33))
        brush = QPainter(self.lblCanvas.pixmap()) # lblCanvas의 브러쉬 객체 생성
        brush.setPen(QPen(self.brushColor, 3.5, style=Qt.SolidLine, cap=Qt.RoundCap))
        brush.drawPoint(e.x(), e.y()-(33))
        brush.end()
        self.update() # 화면 업데이트
    
    
    
    def closeEvent(self, QCloseEvent) -> None: 
        re = QMessageBox.question(self, '종료확인', '종료하시겠습니까?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes :
            QCloseEvent.accept()
        else : 
            QCloseEvent.ignore()

if __name__ =='__main__' :
    app = QApplication(sys.argv)
    ins = windowApp()
    sys.exit(app.exec_())
