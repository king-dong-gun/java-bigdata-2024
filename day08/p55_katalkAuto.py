# file: p55_katalkAuto.py
# desc: 카톡pc에서 자동으로 메시지 보내기

import pyautogui as auto
import pyperclip as clip
import os
import time


try :
    katalkLoc = auto.locateAllOnScreen('./day08/findLoc.png')
    print(katalkLoc)
    clickPos = auto.center(katalkLoc)
    auto.doubleClick(clickPos)
    time.sleep(0.5)
except :
    katalkLoc = auto.locateAllOnScreen('./day08/findLoc2.png')
    clickPos = auto.center


clip.copy('재영이 직이고싶노 ㅋㅋ')
auto.hotkey('command', 'v')
auto.press('\n')