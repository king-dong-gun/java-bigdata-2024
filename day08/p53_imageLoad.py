# file: p53_imageLoad.py
# pyautohui에서 이미지 읽어오기

import pyautogui as auto

# capImg = auto.locateAllOnScreen('./day08/screen.png')
# print(capImg)
# auto.click(capImg)

auto.alert('테스트!!', title = 'PyAutoGui')
auto.confirm('계속 진행하겠습니까?')

text = auto.prompt('원하는 메시지 입력')
print(text)

pwd = auto.password('암호입력')
print(pwd)
