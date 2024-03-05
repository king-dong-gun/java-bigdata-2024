# file: p61_openCv.py
# desc: OpenCV 이미지 처리 계속

import cv2

image = cv2.imread('./images/trash.png', cv2.IMREAD_UNCHANGED) # 원본 이미지

dst = cv2.blur(image, (10, 10), anchor=(-1, -1), borderType=cv2.BORDER_DEFAULT) # 블러(흐림)이미지

# (0, 0): 커널 크기, 이미지의 전체 영역에 대한 평균을 계산하여 블러 효과를 생성
# anchor=(-1, -1): 커널의 중심점을 지정하는 매개변수, (-1, -1)은 커널 중앙을 의미
# borderType=cv2.BORDER_DEFAULT: 이미지의 가장자리 처리 방법을 지정하는 매개변수

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
sobel = cv2.Sobel(gray, cv2.CV_8U, 1, 0, 3)
laplacian = cv2.Laplacian(gray, cv2.CV_8U, ksize=3)
canny = cv2.Canny(image, 100, 255) # 최소 임계값 > 100, 최대 임계값 > 255


height, width, channel = image.shape

cv2.imshow('World Best Trash', image) # 원본 이미지
cv2.imshow('Blur', dst) # 블러 이미지 (흐린 이미지)
cv2.imshow('Sobel', sobel) # 소벨 이미지 (입체감 있는 윤곽)
cv2.imshow('Laplacian', laplacian) # 라플라시안 이미지 (일반적인 윤곽)
cv2.imshow('Canny', canny) # 케니 이미지 (흑백으로 윤곽)

cv2.waitKey(0)
cv2.destroyAllWindows()