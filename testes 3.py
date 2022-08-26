import pyautogui as pg
import os
import time

#pyautogui.alert('Não usar teclado ou mouse enquanto a automação está rodando')
pg.PAUSE = 1

os.startfile(r'C:\PortableApps\PortableApps\GoogleChromePortable\GoogleChromePortable.exe')
time.sleep(5)
pg.write('https://store.epicgames.com/pt-BR/free-games')
pg.press('enter')
#print(pg.position())












time.sleep(60)