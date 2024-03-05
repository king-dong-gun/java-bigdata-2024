# file: p60_openCv.py
# desc: OpenCV 이미지 처리 ~계속

import cv2

image = cv2.imread('./images/trash.png', cv2.IMREAD_UNCHANGED) # 원본 이미지
dst = cv2.flip(image, 0) # 0번은 위아래 반전, 1번은 좌우반전

height, width, channel = image.shape
matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 1) # 이미지의 중앙기준 회전

# cv2.getRotationMatrix2D(center, angle, scale) -> retval
# center: 회전 중심 좌표. (x, y) 튜플.
# angle: (반시계 방향) 회전 각도(degree). 음수는 시계 방향.
# scale: 추가적인 확대 비율
# retval: 2x3 어파인 변환 행렬. 실수형.

thrd = cv2.warpAffine(image, matrix, (width, height))

reversed = cv2.bitwise_not(image) # 색상 반전 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # BGR 컬러 이미지를 그레이 스케일로 변환 
ret, bny = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY) # 이진화 

cv2.imshow('trash', image) # 원본
cv2.imshow('Best trash', dst) # 위아래 반전
cv2.imshow('Rocation', thrd) # 회전
cv2.imshow('Reversed', reversed) # 색상 반전
cv2.imshow('Gray', gray) # 흑백
cv2.imshow('Binary', bny) # 이진화

cv2.waitKey(0)
cv2.destroyAllWindows()