# file: p50_mouseAuto.py
# desc: PyAutoGui로 마우스 조작하기

'''
파이썬 모듈 설치시는 명령 프롬포트보다 VsCode내 터미널에서 설치를 추천
PyAutoGui 모듈 설치
> pip3 install pyautogui
'''

import pyautogui as auto

print(auto.size()) # 현재 모니터 해상도 정보 Size(width: 1920, height: 1080)
print(auto.position()) # 현재 마우스의 위치 좌표

# pyautogui 마우스 설정 창
# pillow 모듈이 같이 설치되어야 색상 표시가능
#auto.mouseInfo()

# 마우스 이동 (절대좌표)
auto.FAILSAFE = False
#auto.moveTo(100,51) #(0,0) 이후 이동X
#auto.moveTo(574,79, duration=1.0) # x축 574, y축 79로 1.0초 동안 이동
#auto.moveTo(1360, 1300, duration=0.1)

# 마우스 이동 (상대좌표)
#auto.move(505,505, duration=1.5) # 현재위치에서 x축 50, y축 50로 1.5초 동안 이동

## 마우스 클릭
#auto.leftClick(x=576, y=78) # 해당위치에서 왼쪽버튼 클릭
#auto.rightClick(x=790, y=300) # 해당위치에서 오른쪽 버튼 클릭
auto.click(clicks=4, interval=0.1, button='left') # 왼쪽버튼을 소스코드 에디터에서 네번 클릭하면 전체 선택

## 마우스 드래그
auto.leftClick(x=1099, y=452, duration=1.0) # 1099, 452에서 왼쪽 마우스 클릭 후 1초 대기
auto.dragTo(x=314, y=705, duration=2.0, button='left')# 절대경로_314,705 이동 후 2초동안 드래그
#auto.dragRel(500, 400, duration=1.0, button='left') # 상대경로_현재위치에서 500,400 이동 후 1초 동안 드래그

## 마우스 휠
auto.scroll(40) # 양수는 위로
auto.scroll(-10) # 음수는 아래로

