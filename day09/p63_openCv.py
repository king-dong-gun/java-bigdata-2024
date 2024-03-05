# file: p63_openCv.py
# desc: OpenCV 영상처리

import cv2

samplePath = './images/antonyTurn.mp4' # 동영상 파일 가져오가
cap = cv2.VideoCapture(samplePath) # 동영상 파일 열기

while True :
    ret, frame = cap.read()

    if not ret :
        cap = cv2.VideoCapture(samplePath)
        continue


    ## 영상 편집
    blur = cv2.blur(frame, (15, 15))
    flip = cv2.flip(frame, 1)

    cv2.imshow('original', frame)
    cv2.imshow('blur', blur)
    cv2.imshow('flip', flip)

    key = cv2.waitKey(5)
    if key == 27 : # esc(27) > 루프 종료, ord('q') > q 루프 종료
        break
    elif key == ord('c') : # 화면 캡쳐
        cv2.imwrite('./day09/hmba.jpg', frame)

cap.release() # 캡쳐 객체 해제
cv2.destroyAllWindows()
