# file: p59_openCv.py
# desc: OpenCV 활용

# OpenCV 실시간 이미지 프로세싱 라이브러리
'''
> pip3 install opencv-python
'''

import cv2

# print(cv2.__version__) # OpenCV 설치 확인용

image = cv2.imread('./images/trash.png', cv2.IMREAD_UNCHANGED) # cv2.IMREAD_GRAYSCALE -> 칼라이미지를 흑백으로 변환
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # 원본을 흑백으로 변경


height, width, channel = image.shape
print(width, height, channel)

sizeSmall = cv2.resize(image, (width//2, height//2)) 

# img_cropped = image[:(height//2), :(width//2)] # x축, y축
img_cropped = image[:, :(width//2)] # x축을 반으로 자르기ßßß

cv2.imshow('Antony~, color', image) # 원본
cv2.imshow('SmallTony~', sizeSmall) # 반으로 줄인 사이즈
cv2.imshow('Antony~, gray', gray) # 흑백
cv2.imshow('HalfTony~', img_cropped) # 사진 자르기

cv2.waitKey(0) # 
cv2.destroyAllWindows() # 열린 창 모두 닫기