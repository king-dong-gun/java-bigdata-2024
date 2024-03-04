# file: p51_keyboard.py
# desc: PyAutoGui로 키보드 조작하기

'''
한글 입력은 pyperclip
> pip3 install pyperclip
'''

import pyautogui as auto
import pyperclip as clip

#auto.mouseInfo()
#auto.click(377, 765)
auto.write("print('ManUnited')", interval=0.01)
auto.write("\n", interval=0.01)
#auto.write(['M','a','n','U'])
auto.typewrite("print('Groly')", interval=0.01) # write와 동일

## 키보드 프레스 기능
auto.press('enter')
auto.press('A')

## 키보드 단축키로 입력
#auto.hotkey('command', 'a') # 전체선택
#auto.hotkey('command', 'c') # 복사하기
#auto.press('esc')

#auto.press('\n'); auto.press('\n'); auto.press('\n')

#auto.hotkey('command', 'v') # 붙여넣기

# 한글은 pyautogui에서 입력할 수 없음
clip.copy('맨체스터는 붉은색입니다.') # 클립보드에 한글 내용을 저장
auto.hotkey('command', 'v') # 붙여넣기

