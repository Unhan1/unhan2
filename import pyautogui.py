import pyautogui
import time

#location = pyautogui.locateOnScreen('cuche.png')
#print('location')

center = pyautogui.locateCenterOnScreen('cuche.PNG')
pyautogui.click(center)


kakao = 'xjar.PNG'
# 이미지가 나타날 때까지 기다리기
while True:
    # 화면에서 이미지 찾기
    location = pyautogui.locateOnScreen(kakao)
    if location is not None:
        zero = pyautogui.locateCenterOnScreen('xjar.PNG')
        pyautogui.click(zero)
        break
    else:
        # 이미지가 발견되지 않으면 0.2초 대기 후 다시 시도
        time.sleep(0.1)


pyautogui.press('end')
time.sleep(0.05)
pyautogui.press('end')
time.sleep(0.1)
pyautogui.press('end')
time.sleep(0.05)
pyautogui.press('end')
time.sleep(0.1)
pyautogui.press('end')
time.sleep(0.05)
pyautogui.press('end')
time.sleep(0.1)
pyautogui.press('end')
time.sleep(0.04)
pyautogui.press('end')
time.sleep(0.13)
pyautogui.press('end')
time.sleep(0.05)

pyautogui.hotkey('ctrl', 'f')

time.sleep(0.5)

#pyautogui.typewrite('sh', interval=0.1)
pyautogui.press('enter')
