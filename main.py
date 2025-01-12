import pyautogui
import time

pyautogui.PAUSE = 1

time.sleep(10)
# verificar se o mouse esta na area de trabalho principal
pyautogui.hotkey('win', 'ctrl', 'right')
pyautogui.hotkey('win', 'ctrl', 'right')
# comando para mudar a area de trabalho
pyautogui.hotkey('win', 'ctrl', 'left')

# abre o google chrome
pyautogui.click(x=958, y=1060)
pyautogui.hotkey('win', 'up')

# clica na agenda e arrasta para a direita
pyautogui.click(x=332, y=31, duration=0.5)
pyautogui.dragTo(x=1920, y=500, duration=0.5)

# clica na segunda pagina
pyautogui.click(x=419, y=548, duration=0.5)
pyautogui.scroll(-1000)	
time.sleep(1)
pyautogui.click(x=1512, y=138)
pyautogui.click(x=1519, y=181)
pyautogui.click(x=1568, y=136)

# abrindo alguns apliucativos
pyautogui.press('win')
pyautogui.write('TickTick')
pyautogui.press('enter')
time.sleep(0.5)
pyautogui.press('win')
pyautogui.write('WhatsApp')
pyautogui.press('enter')
time.sleep(1)

# comando para voltar a area de trabalho principal
pyautogui.hotkey('win', 'ctrl', 'right')

# abre o notion
pyautogui.hotkey('alt', 'space')
pyautogui.write('https://www.notion.so/Segundo-C-rebro-fc2adc1edbd1479cb87de49c6bbb4e63')
pyautogui.press('enter')
pyautogui.hotkey('win', 'up')