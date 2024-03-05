# file: p63_openCv.py
# desc: OpenCV news 영상처리

import cv2

samplePath = './images/news.mp4' # 동영상 파일 가져오가
faceCascade = cv2.CascadeClassifier('./day09/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(samplePath) # 동영상 파일 열기

while True :
    ret, frame = cap.read()

    if not ret :
        cap = cv2.VideoCapture(samplePath)
        continue


    ## 영상 편집 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (20, 20)
    )
    for (x, y, w, h) in faces :
        cv2.rectangle(frame, pt1=(x, y), pt2=(x + w, y + h), color=(255, 0 , 0), thickness=2) # color=(Blue, Green , Red)

    cv2.imshow('original', frame) # 옆 화면이나 화질이 안좋거나, 색상이 없는 경우 인식이 잘 안됨
    cv2.imshow('Gray', gray)


    key = cv2.waitKey(5)
    if key == 27 : # esc(27) > 루프 종료, ord('q') > q 루프 종료
        break

cap.release() # 캡쳐 객체 해제
cv2.destroyAllWindows()
