# file: p52_screenCap.py
# desc: pyautogui로 화면 캡쳐하기

'''
> pip3 install pillow
'''
import pyautogui as auto
import time

startX, endX = 0, 1919
startY, endY = 0, 1079

img = auto.screenshot('./day08/screen.png', region=(startX, startY, endX-startY, endY-startY)) # 스크린샷 찍기
img.save("./day08/screen.png") # 저장하기

