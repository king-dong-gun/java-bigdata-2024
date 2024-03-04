# file: p54_capWeather.py
# desc: 날씨사진 캡쳐

import pyautogui as auto
import pyperclip as clip
import time

regions = ['서울', '대전', '대구', '부산', '울산']

# auto.mouseInfo() # 520, 149
for region in regions :
    auto.moveTo(520, 149, duration=0.5)
    auto.leftClick()
    for _ in range(5) :
        auto.press('backspace')
        auto.press('delete')
    time.sleep(0.2)

    clip.copy(f'{region} 날씨')
    auto.hotkey('command', 'v') # 붙여넣기
    time.sleep(0.2)

    auto.press('enter') # \n 도 가능
    time.sleep(1.0)

    startX, startY = 401, 269
    endX, endY = 1073, 914

    # auto.screenshot()만 사용하면 mac Os에서 동작X
    img = auto.screenshot(f'./day08/{region}날씨.png', region=(startX, startY, endX-startX, endY-startY))
    img.save(f"./day08/{region}날씨.png")

    print(f'{region}저장완료!')



